# from django.db import models
# from account.models import Profile
# from book.models import Book

# class UserCollection(models.Model):
#     user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     books = models.ManyToManyField(Book, related_name='collections', blank=True)
#     reviews = models.TextField(blank=True)
    
#     def add_book_to_collection(self, book):
#         if self.books.count() < 10 and not book.is_borrowed:
#             self.books.add(book)
#             book.is_borrowed = True
#             book.save()

#     def remove_book_from_collection(self, book):
#         self.books.remove(book)
#         book.is_borrowed = False
#         book.save()

#     def __str__(self):
#         return f"Collection of {self.user_profile.user.username}"

from django.db import models
from account.models import Profile
from book.models import Book

class Collection(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='CollectionBook')

    def __str__(self):
        return self.name

class CollectionBook(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.collection.name} - {self.book.title}"
