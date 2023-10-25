from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User

@login_required(login_url='account/login')
def show_main(request):
    if request.user.role == User.ADMIN:
        return render(request, "landing_page_admin.html")
    
    elif request.user.role == User.USER:
        return render(request, "landing_page_user.html")

# Create your views here.
