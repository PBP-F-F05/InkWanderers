import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Collection, CollectionBook
from book.models import Book
from account.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse
from account.models import Rank_Book, Rank_Book_To_Book, History_Book, History_Book_To_Book

@login_required
def my_collections(request):
    owner = Profile.objects.get(user=request.user)
    collection = Collection.objects.filter(owner=owner)[0]
    collection_book = CollectionBook.objects.filter(collection = collection)
    context = {
        'collection_book': collection_book,
    }
    return render(request, 'my_collection.html', context)

@login_required
def add_book_to_collection(request, book_id):
    
    book = Book.objects.filter(pk=book_id)[0]
    owner = Profile.objects.filter(user=request.user)[0]
    collection = Collection.objects.filter(owner=owner)[0]
    

    # Maksimal 10 buku dalam satu koleksi
    if CollectionBook.objects.filter(collection=collection).count() >= 10:
        messages.error(request, 'Koleksi ini telah mencapai batas maksimal.')
    else:
        book.is_borrowed = True
        book.save()
        rank_book = Rank_Book.objects.filter(profile = owner)[0]
        history_book = History_Book.objects.filter(profile = owner)[0]
        if(Rank_Book_To_Book.objects.filter(rank_book = rank_book, book = book).exists() ):
            rank_book_to_book_user = Rank_Book_To_Book.objects.filter(rank_book = rank_book, book = book)[0]
            rank_book_to_book_user.books_count += 1
            history_book_to_book_user = History_Book_To_Book(history_book = history_book, book = book)
        else:
            rank_book_to_book_user = Rank_Book_To_Book(rank_book = rank_book, book = book, books_count = 1)
            history_book_to_book_user = History_Book_To_Book(history_book = history_book, book = book)

        collection = Collection.objects.filter(owner=owner)[0]
        collection_book = CollectionBook(collection=collection, book=book)
        collection.save()
        collection_book.save()
        rank_book_to_book_user.save()
        history_book_to_book_user.save()


    return redirect('main:show_main')

@login_required
def remove_book_from_collection(request, collection_book_id):

    owner = Profile.objects.get(user = request.user)
    collection = Collection.objects.filter(owner = owner)[0]
    book = Book.objects.filter(id = collection_book_id)[0]
    collection_book = CollectionBook.objects.filter(book = book)[0]

    if collection_book.collection.owner == owner:
        # collection_book.book.is_borrowed = False
        # collection_book.book.save()
        # collection_book.delete()
        # collection.save()

        return redirect('reviews:add_review', collection_book_id)
    
#--------------------------------------------------------------------------#
#-------------------------- Flutter Function ------------------------------#
#--------------------------------------------------------------------------#
    
@csrf_exempt
def collections_flutter(request):
    owner = Profile.objects.get(user=request.user)
    collection = Collection.objects.get(owner=owner)
    collection_books = CollectionBook.objects.filter(collection=collection)
    books = [cb.book for cb in collection_books]
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

@csrf_exempt
def add_collection_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.filter(pk=data["pk"])[0]
        owner = Profile.objects.filter(user=request.user)[0]
        collection = Collection.objects.filter(owner=owner)[0]

        if CollectionBook.objects.filter(collection=collection).count() >= 10:
            return JsonResponse({
                "status": False,
                "message": 'Koleksi ini telah mencapai batas maksimal.',
            }, status=200)
        
        book.is_borrowed = True
        book.save()
        rank_book = Rank_Book.objects.filter(profile = owner)[0]
        history_book = History_Book.objects.filter(profile = owner)[0]
        if(Rank_Book_To_Book.objects.filter(rank_book = rank_book, book = book).exists() ):
            rank_book_to_book_user = Rank_Book_To_Book.objects.filter(rank_book = rank_book, book = book)[0]
            rank_book_to_book_user.books_count += 1
            history_book_to_book_user = History_Book_To_Book(history_book = history_book, book = book)
        else:
            rank_book_to_book_user = Rank_Book_To_Book(rank_book = rank_book, book = book, books_count = 1)
            history_book_to_book_user = History_Book_To_Book(history_book = history_book, book = book)

        collection_book = CollectionBook(collection=collection, book=book)
        collection.save()
        collection_book.save()
        rank_book_to_book_user.save()
        history_book_to_book_user.save()
        return JsonResponse({
                "status": True,
                "message": 'Koleksi berhasil ditambahkan',
            }, status=200)
    
    return JsonResponse({
                "status": False,
                "message": 'Koleksi gagal ditambahkan',
            }, status=500)

@csrf_exempt   
def remove_collection_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        owner = Profile.objects.get(user = request.user)
        collection = Collection.objects.get(owner = owner)
        book = Book.objects.get(pk = int(data["pk"]))
        collection_book = CollectionBook.objects.get(book = book, collection = collection)
        collection_book.delete()
        book.is_borrowed = False
        book.save()
        return JsonResponse({
            "status": True,
            "message": 'Review berhasil di submit',
        }, status=200)

    return JsonResponse({
        "status": False,
        "message": 'Review gagal di submit',
    }, status=500)
