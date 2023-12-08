from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from account.models import *

@csrf_exempt
def login(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Status login sukses.
                print('sukses')
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!"
                    # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, akun dinonaktifkan."
                }, status=401)

        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali email atau kata sandi."
            }, status=401)

    else:
        return JsonResponse({
            "statusCode": 404,
                "message": "Unknown request."
            }, status=404)    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            print("Line 71")
            return JsonResponse({
                "status": False,
                "message": "Register gagal, username sudah digunakan."
            }, status=400)

        # Create new user
        user = User.objects.create_user(username=username, password=password)
        user.role = role

        user.save()

        return JsonResponse({
            "username": user.username,
            "status": True,
            "message": "Register berhasil!"
        }, status=201)

    else:
        print("Line 90")
        return JsonResponse({
            "status": False,
            "message": "Invalid request"
        }, status=400)