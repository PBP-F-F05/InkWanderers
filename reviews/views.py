import json
from django.shortcuts import render
from reviews.models import Review, ReviewSerializer
from book.models import Book
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from reviews.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from collection.models import CollectionBook, Collection
from account.models import BookSerializer, Profile
@login_required
def show_review(request, id):
    book = Book.objects.get(pk=id)
    reviews = Review.objects.filter(book = book)
    context = {
        'reviews':reviews,
        'book':book
    }
    return render(request, 'reviews.html',context)
@login_required
def add_review(request, id):
    form = ProductForm(request.POST or None)
    profile = Profile.objects.filter(user=request.user)[0]
    book = Book.objects.get(pk = id)
    collection = Collection.objects.filter(owner=profile)[0]
    if CollectionBook.objects.filter(book = book, collection = collection).exists():
        if form.is_valid() and request.method == "POST":
            collection = Collection.objects.filter(owner = profile)[0]
            collection_book = CollectionBook.objects.filter(book = book)[0]
            collection_book.book.is_borrowed = False
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            collection_book.book.review_count+=1
            collection_book.book.review_points+=review.rating
            collection_book.book.save()
            collection_book.delete()
            collection.save()
            review.save()
            # book.save()
            return HttpResponseRedirect(reverse('reviews:show_review', args=[id]))
    context = {'form': form, 'book':book}
    return render(request, "add_review.html", context)
@login_required
def show_my_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    book = Book.objects.all()
    context = {
        'reviews':reviews,
        'book':book
    }
    return render(request, 'my_reviews.html', context)

def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Review.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.serializers import get_serializer
def show_json_flutter(request):
    data= Review.objects.all()
    serializer = ReviewSerializer(data, many=True)
    return HttpResponse(serializer.data, content_type="application/json")
@api_view(('GET',))
@csrf_exempt
def get_review_json(request):
    data = Review.objects.filter(user=request.user)
    serializer = ReviewSerializer(data, many=True)
    return JsonResponse(data=serializer.data, safe=False)

@csrf_exempt
def edit_review_ajax(request, id):
    if request.method == "POST":
        review = Review.objects.get(pk=id)
        book = Book.objects.get(pk=review.book.pk)
        rating = request.POST.get("rating")
        reviewText = request.POST.get("review")
        book.review_points -= review.rating
        book.review_points += int(rating)
        review.rating = int(rating)
        review.review = reviewText
        review.save()
        book.save()
        return HttpResponse(status=200)
    return HttpResponseNotFound()

@login_required
@csrf_exempt
def add_review_flutter(request, id):
    if request.method == 'POST':
        
        # profile = Profile.objects.filter(user=request.user)[0]
        # collection = Collection.objects.filter(owner=profile)[0]
        data = json.loads(request.body)
        # id2 = int(data['pk'])
        book = Book.objects.get(pk = id)
        # collection = Collection.objects.filter(owner = profile)[0]
        # collection_book = CollectionBook.objects.filter(book = book)[0]
        # collection_book.book.is_borrowed = False
        new_product = Review.objects.create(
            user = request.user,
            book = book,
            rating = int(data["rating"]),
            review = data["review"]
        )
        new_product.save()
        # collection_book.book.review_count+=1
        # collection_book.book.review_points+= new_product.rating
        # collection_book.book.save()
        # collection_book.delete()
        # collection.save()
        book.review_points += int(data["rating"])
        book.review_count += 1
        book.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def show_review_by_book(request, id):
    book = Book.objects.get(pk=id)
    data = Review.objects.filter(book = book)
    serializer = ReviewSerializer(data, many=True)
    return JsonResponse(data=serializer.data, safe=False)

def get_book_json_id(request, id):
    data = Book.objects.get(pk=id)
    return HttpResponse(serializers.serialize("json", [data]), content_type="application/json")

@csrf_exempt
def edit_review_flutter(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        review = Review.objects.get(pk=id)
        book = Book.objects.get(pk=review.book.pk)
        rating = data["rating"]
        reviewText = data["review"]
        book.review_points -= review.rating
        book.review_points += int(rating)
        review.rating = int(rating)
        review.review = reviewText
        review.save()
        book.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)