from django.db import models
from django.contrib.auth.models import User  
from book.models import Book
from account.models import Profile

class BookmarkList(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bookmarked_books = models.ManyToManyField(Book)
    bookmarked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark list for {self.user.username}"
