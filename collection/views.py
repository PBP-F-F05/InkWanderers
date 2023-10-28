# from django.shortcuts import render, redirect
# from .models import UserCollection
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from book.models import Book

# @login_required
# def user_collection(request):
#     user_profile = request.user.profile

#     if not UserCollection.objects.filter(user_profile=user_profile).exists():
#         UserCollection.objects.create(user_profile=user_profile)

#     collection = UserCollection.objects.get(user_profile=user_profile)

#     if request.method == 'POST':
#         book_id = request.POST.get('book_id')
#         book = Book.objects.get(id=book_id)

#         if collection.books.count() >= 10:
#             messages.error(request, 'Koleksi Anda sudah mencapai maksimum (10 buku).')
#         else:
#             collection.add_book_to_collection(book)
#             messages.success(request, f'{book.title} berhasil ditambahkan ke koleksi Anda.')

#     return render(request, 'collection.html', {'collection': collection})

# @login_required
# def remove_book(request, book_id):
#     user_profile = request.user.profile
#     collection = UserCollection.objects.get(user_profile=user_profile)
#     book = Book.objects.get(id=book_id)

#     if book in collection.books.all():
#         collection.remove_book_from_collection(book)
#         messages.success(request, f'{book.title} berhasil dihapus dari koleksi Anda.')

#     return redirect('user_collection')

# @login_required
# def add_review(request, collection_id):
#     user_profile = request.user.profile
#     collection = UserCollection.objects.get(user_profile=user_profile)

#     if request.method == 'POST':
#         review = request.POST.get('review')
#         collection.reviews = review
#         collection.save()
#         messages.success(request, 'Ulasan berhasil ditambahkan.')

#     return redirect('user_collection')

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
