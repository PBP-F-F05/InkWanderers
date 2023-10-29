from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Collection, CollectionBook
from book.models import Book
from account.models import Profile
from django.contrib.auth.decorators import login_required
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
        collection_book.book.is_borrowed = False
        collection_book.book.save()
        collection_book.delete()
        collection.save()

    return redirect('reviews:add_review', collection_book_id)
