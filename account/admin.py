from django.contrib import admin
from account.models import User, Profile, History_Book, History_Book_To_Book, Rank_Book, Rank_Book_To_Book
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(History_Book)
admin.site.register(History_Book_To_Book)
admin.site.register(Rank_Book)
admin.site.register(Rank_Book_To_Book)