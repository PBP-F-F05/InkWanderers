from http.client import HTTPResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login

from .models import User
from django.contrib.auth import authenticate
from django.contrib import messages  
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required
from account.forms import SignUpForm
from django.contrib.auth import logout
from account.models import User, Profile
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.role = request.POST['role']
            print("line 30 ->",user.role)
            user.save()
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return JsonResponse({"success": True, "message": "Your account has been successfully created!"})

        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors})

    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("account:profile")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response            

        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('account:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required
def profile(request):
    profile = Profile.objects.filter(user = request.user)[0]
    context = {
               'profile':profile
               }
    return render(request, 'profile.html', context)

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Updating the user's session to avoid logging them out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated.')
            return redirect(reverse('account:profile'))
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'password_change.html', {'form': form})

@login_required
def password_change_by_ajax(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Updating the user's session to avoid logging them out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated.')
            return redirect(reverse('account:profile'))
    else:
        form = PasswordChangeForm(user=request.user)

    return HttpResponseNotFound()

from book.models import Book
@login_required
def view_books(request):
    books = Book.objects.all()
    context={
        'books':books
    }
    return render(request, 'view_books.html', context)

from account.models import Rank_Book, Rank_Book_To_Book,History_Book, History_Book_To_Book
@login_required
def add_book(request, id):
    user = request.user
    books = Book.objects.all()
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)  # Use get() to retrieve a single profile
        book = Book.objects.filter(id=id)[0]  # Use get() to retrieve a single book
        rank_book = Rank_Book.objects.filter(profile = profile)[0]
        history_book = History_Book.objects.filter(profile = profile)[0]
        if(Rank_Book_To_Book.objects.filter(rank_book = rank_book, book = book).exists() ):
            rank_book_to_book_user = Rank_Book_To_Book.objects.filter(rank_book = rank_book, book = book)[0]
            rank_book_to_book_user.books_count += 1
            history_book_to_book_user = History_Book_To_Book(history_book = history_book, book = book)
        else:
            rank_book_to_book_user = Rank_Book_To_Book(rank_book = rank_book, book = book, books_count = 1)
            history_book_to_book_user = History_Book_To_Book(history_book = history_book, book = book)

        rank_book_to_book_user.save()
        history_book_to_book_user.save()


    return redirect('account:view_books')

@login_required
def view_rank_book(request):
    user = request.user
    profile = Profile.objects.filter(user = user)[0]
    rank_book = Rank_Book.objects.filter(profile = profile)[0]
    rank_book_to_book_by_highest_number = Rank_Book_To_Book.objects.filter(rank_book = rank_book).order_by('-books_count')
    context={
        'rank_book_to_book':rank_book_to_book_by_highest_number
    }
    return render(request, 'rank_book.html', context)
@login_required
def view_history_book(request):
    user = request.user
    profile = Profile.objects.filter(user = user)[0]
    history_book = History_Book.objects.filter(profile = profile)[0]
    history_book_to_book = History_Book_To_Book.objects.filter(history_book = history_book)
    context={
        'history_book_to_book':history_book_to_book
    }
    return render(request, 'history_book.html', context)

from django.core import serializers
from django.http import HttpResponse
from account.models import RankBookToBookSerializer, HistoryBookToBookSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view
@api_view(('GET',))
def show_json_by_highest_number(request):
    user = request.user
    profile = Profile.objects.filter(user = user)[0]
    rank_book = Rank_Book.objects.filter(profile = profile)[0]
    data = Rank_Book_To_Book.objects.filter(rank_book = rank_book).order_by('-books_count')
    serializer = RankBookToBookSerializer(data, many=True)

    return Response(data = serializer.data)

@api_view(('GET',))
def show_json_history_book(request):
    user = request.user
    profile = Profile.objects.filter(user = user)[0]
    history_book = History_Book.objects.filter(profile = profile)[0]
    data = History_Book_To_Book.objects.filter(history_book = history_book).order_by('-pk')
    serializer = HistoryBookToBookSerializer(data, many=True)

    return Response(data = serializer.data)