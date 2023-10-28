from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Collection, CollectionBook
from book.models import Book
from account.models import Profile
from django.contrib.auth.decorators import login_required

@login_required
def create_collection(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        owner = Profile.objects.get(user=request.user)

        # Maksimal 10 buku dalam koleksi
        if Collection.objects.filter(owner=owner).count() >= 10:
            messages.error(request, 'Anda telah mencapai batas maksimal koleksi.')
        else:
            collection = Collection(name=name, owner=owner)
            collection.save()
            messages.success(request, 'Koleksi berhasil dibuat.')

        return redirect('collection:my_collections')
    return render(request, 'create_collection.html')

@login_required
def my_collections(request):
    owner = Profile.objects.get(user=request.user)
    collections = Collection.objects.filter(owner=owner)
    context = {
        'collections': collections,
    }
    return render(request, 'my_collections.html', context)

@login_required
def add_book_to_collection(request, collection_id, book_id):
    collection = Collection.objects.get(pk=collection_id)
    book = Book.objects.get(pk=book_id)
    owner = Profile.objects.get(user=request.user)

    # Maksimal 10 buku dalam satu koleksi
    if CollectionBook.objects.filter(collection=collection).count() >= 10:
        messages.error(request, 'Koleksi ini telah mencapai batas maksimal.')
    else:
        collection_book, created = CollectionBook.objects.get_or_create(collection=collection, book=book)

        # Jika buku berhasil ditambahkan ke koleksi, tandai buku sebagai "is_borrowed" False
        if created:
            book.is_borrowed = False
            book.save()
            messages.success(request, 'Buku berhasil ditambahkan ke koleksi.')

    return redirect('collection:my_collections')

@login_required
def remove_book_from_collection(request, collection_id, collection_book_id):
    collection = Collection.objects.get(pk=collection_id)
    owner = Profile.objects.get(user=request.user)
    collection_book = CollectionBook.objects.get(pk=collection_book_id)

    if collection_book.collection.owner == owner:
        collection_book.delete()

        # Tandai buku sebagai "is_borrowed" True jika tidak ada lagi di koleksi
        if not CollectionBook.objects.filter(book=collection_book.book).exists():
            collection_book.book.is_borrowed = True
            collection_book.book.save()

        messages.success(request, 'Buku berhasil dihapus dari koleksi.')
    else:
        messages.error(request, 'Anda tidak memiliki izin untuk menghapus buku dari koleksi ini.')

    return redirect('collection:my_collections')
