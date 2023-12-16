from django.db import models
from book.models import Book
from account.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

from rest_framework import serializers
from account.models import BookSerializer, UserSerializer
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()

    class Meta:
        model = Review
        fields = '__all__'