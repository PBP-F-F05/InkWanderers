from audioop import reverse
import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from account.models import User
from book.models import Book
from bookmarks.models import BookmarkList
from account.models import Profile

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



@csrf_exempt
def get_books_json(request):
    if request.user.role == User.ADMIN:
        books = Book.objects.all()
        
    elif request.user.role == User.USER:
        books = Book.objects.filter(is_borrowed=False)
    
    return HttpResponse(serializers.serialize('json', books))

@csrf_exempt
def create_book_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        print(data)

        new_product = Book.objects.create(
            title = data["title"],
            authors = data["authors"],
            categories = data["categories"],
            thumbnail =  data["thumbnail"],
            description = data["description"],
            published_year = int(data["published_year"])
        )

        new_product.save()
        print("Book added to catalogue")
        return JsonResponse({"status": "success"}, status=200)
    
    else:
        print("gagal")
        return JsonResponse({"status": "error"}, status=401)
    
    
@csrf_exempt
def remove_book_flutter(request):
    if request.user.role == User.ADMIN:
        data = json.loads(request.body)
        book = Book.objects.get(pk=data["pk"])
        book.delete()
        return JsonResponse({"status": "success"}, status=200)
        
    else:
        return JsonResponse({"status": "error"}, status=403)