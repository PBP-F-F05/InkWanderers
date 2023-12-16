import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import BookmarkList
from book.models import Book
from account.models import Profile
from django.core import serializers
from account.models import User
from django.views.decorators.csrf import csrf_exempt


@login_required
def view_bookmarks(request):
    user = Profile.objects.get(user=request.user)
    bookmark_list, created = BookmarkList.objects.get_or_create(user=user)
    bookmarked_books = bookmark_list.bookmarked_books.all()
    
    context = {
        'bookmarked_books': bookmarked_books
    }

    return render(request, 'bookmarks/view_bookmarks.html', context)

def bookmark_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        user = Profile.objects.get(user=request.user)
        bookmark = BookmarkList.objects.filter(user=user)[0]
        bookmark_list, created = BookmarkList.objects.get_or_create(user=user)

        if book not in bookmark_list.bookmarked_books.all():
            bookmark_list.bookmarked_books.add(book)
            # messages.success(request, 'Buku telah ditandai sebagai bookmark.')
        return redirect('main:show_main')
    except Book.DoesNotExist:
        # messages.error(request, 'Buku tidak ditemukan.')
        return redirect('main:show_main')

@login_required
def remove_bookmark(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        user = Profile.objects.get(user=request.user)
        bookmark_list, created = BookmarkList.objects.get_or_create(user=user)

        if book in bookmark_list.bookmarked_books.all():
            bookmark_list.bookmarked_books.remove(book)

        return redirect('view_bookmarks')
    except Book.DoesNotExist:
        # messages.error(request, 'Buku tidak ditemukan.')
        return redirect('view_bookmarks')

from rest_framework.decorators import api_view

@api_view(('GET',))
def get_books_json(request):     
    user = Profile.objects.get(user=request.user)[0]
    books = BookmarkList.objects.filter(user=user)
    data = BookmarkList.objects.filter(bookmarked_books=books).order_by('-pk')

    return HttpResponse(serializers.serialize('json', books))

#flutter stuff

def get_bookmarks(request):
    user = Profile.objects.get(user = request.user)
    bookmark_list, created = BookmarkList.objects.get_or_create(user=user)
    bookmarked_books = bookmark_list.bookmarked_books.all()
    return HttpResponse(serializers.serialize('json', bookmarked_books), content_type="application/json")

@csrf_exempt
def bookmark_book_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=data["pk"])
        user = Profile.objects.get(user=request.user)
        bookmark_list, created = BookmarkList.objects.get_or_create(user=user)
        if book in bookmark_list.bookmarked_books.all():
            return JsonResponse({
                "status": False,
            }, status=500)  
            
        bookmark_list.bookmarked_books.add(book)
        return JsonResponse({
            "status": True,
        }, status=200)
    
    return JsonResponse({
        "status": False,
    }, status=500)  

@csrf_exempt 
def remove_bookmark_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(request.user)
        print(data["pk"])
        book = Book.objects.get(pk=data["pk"])
        user = Profile.objects.get(user=request.user)
        bookmark_list, created = BookmarkList.objects.get_or_create(user=user)
        bookmark_list.bookmarked_books.remove(book)
        return JsonResponse({
            "status": True,
        }, status=200)

    return JsonResponse({
        "status": False,
    }, status=500) 