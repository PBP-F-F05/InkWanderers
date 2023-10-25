from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

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
      following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True, null=True)
      profile_picture_url = models.CharField(max_length=512, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')

      def __str__(self):
        return self.user.username
      
from book.models import Book
class History_Book(models.Model):
     profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)

class History_Book_To_Book(models.Model):
    history_book = models.ForeignKey(History_Book, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    books_count = models.PositiveIntegerField(default=0)


