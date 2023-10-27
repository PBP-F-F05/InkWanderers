from audioop import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from account.models import User
from book.models import Book

@login_required(login_url='account/login')
def show_main(request):
    if request.user.role == User.ADMIN:
        products = Book.objects.all()
        context = {
            'role': 'Admin',
            'name': request.user.username,
            'products': products,
        }
        return render(request, "landing_page_admin.html", context)
    
    elif request.user.role == User.USER:
        products = Book.objects.filter(is_borrowed=False)
        context = {
            'role': 'User',
            'name': request.user.username,
            'products': products,
        }
        return render(request, "landing_page_user.html", context)
    

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        authors = request.POST.get("authors")
        categories = request.POST.get("categories")
        thumbnail =  request.POST.get("thumbnail")
        description = request.POST.get("description")
        published_year = request.POST.get("published_year")
        
        new_product = Book(title=title, authors=authors, categories=categories, thumbnail=thumbnail, description=description, published_year=published_year)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


@csrf_exempt
def remove_book_ajax(request, id):
    if request.user.role == User.ADMIN:
        Book.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("main:show_main"))



def get_books_json(request):
    if request.user.role == User.ADMIN:
        books = Book.objects.all()
        
    elif request.user.role == User.USER:
        books = Book.objects.filter(is_borrowed=False)
    
    return HttpResponse(serializers.serialize('json', books))