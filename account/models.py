from django.db import models

# Create your models here.
from django.db import models

# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, Permission
class User(AbstractUser):
      ADMIN = 1
      USER = 2
      
      ROLE_CHOICES = (
          (ADMIN, 'Admin'),
          (USER, 'User'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
          

class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
      profile_picture_url = models.CharField(max_length=512, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
      limit_rent = models.IntegerField(default=10)
      def __str__(self):
        return self.user.username
      
#  Class for book rank
from book.models import Book
class Rank_Book(models.Model):
     profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

class Rank_Book_To_Book(models.Model):
    rank_book = models.ForeignKey(Rank_Book, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    books_count = models.PositiveIntegerField(default=0)

# Class for history of book of the user
class History_Book(models.Model):
     profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

class History_Book_To_Book(models.Model):
    history_book = models.ForeignKey(History_Book, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)


# === Flutter Serializer ===
from .models import Book, History_Book_To_Book
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class HistoryBookToBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = History_Book_To_Book
        fields = '__all__'

class RankBookToBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Rank_Book_To_Book
        fields = '__all__'

