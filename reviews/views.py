from django.shortcuts import render
from reviews.models import Review
from book.models import Book
# Create your views here.
from django.http import HttpResponseRedirect
from reviews.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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
    book = Book.objects.get(pk = id)
    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.user = request.user
        review.book = book
        book.review_count+=1
        book.review_points+=review.rating
        review.save()
        book.save()
        return HttpResponseRedirect(reverse('reviews:show_review', args=[id]))
    context = {'form': form}
    return render(request, "add_review.html", context)
@login_required
def show_my_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    context = {
        'reviews':reviews
    }
    return render(request, 'my_reviews.html', context)

def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Review.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    review_item = Review.objects.all()
    return HttpResponse(serializers.serialize('json', review_item))
@csrf_exempt
def delete_review_ajax(request, id):
    review = Review.objects.get(pk=id)
    review.delete()
    return HttpResponse(status=204)
