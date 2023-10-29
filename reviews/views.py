from django.shortcuts import render
from reviews.models import Review, ReviewSerializer
from book.models import Book
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound
from reviews.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from collection.models import CollectionBook, Collection
from account.models import Profile
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


@api_view(('GET',))
def get_review_json(request):
    data = Review.objects.filter(user=request.user)
    serializer = ReviewSerializer(data, many=True)
    return Response(data=serializer.data)

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
