from django.contrib import admin
from account.models import User, Profile, History_Book
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(History_Book)