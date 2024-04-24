from django.db import models

class BookModel(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)

    price = models.FloatField()
    pages = models.PositiveSmallIntegerField()