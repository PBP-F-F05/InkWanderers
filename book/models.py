from django.db import models

class Book(models.Model) :
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    thumbnail =  models.TextField()
    description = models.TextField()
    published_year = models.IntegerField()

    def __str__(self):
        return self.title
    