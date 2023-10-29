from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import BookmarkList
from book.models import Book
from account.models import Profile

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
            messages.success(request, 'Buku telah ditandai sebagai bookmark.')
        else:
            messages.info(request, 'Buku sudah ditandai sebagai bookmark sebelumnya.')

        return redirect('main:show_main')
    except Book.DoesNotExist:
        messages.error(request, 'Buku tidak ditemukan.')
        return redirect('main:show_main')

@login_required
def remove_bookmark(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        user = Profile.objects.get(user=request.user)
        bookmark_list, created = BookmarkList.objects.get_or_create(user=user)

        if book in bookmark_list.bookmarked_books.all():
            bookmark_list.bookmarked_books.remove(book)
            messages.success(request, 'Buku telah dihapus dari bookmark.')
        else:
            messages.info(request, 'Buku tidak ditemukan di bookmark.')

        return redirect('view_bookmarks')
    except Book.DoesNotExist:
        messages.error(request, 'Buku tidak ditemukan.')
        return redirect('view_bookmarks')
    





