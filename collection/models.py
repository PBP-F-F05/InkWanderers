from django.db import models
from account.models import Profile
from book.models import Book

class Collection(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # books = models.ForeignKey(Book, on_delete=models.CASCADE)

class CollectionBook(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title}"
