from django.db import models

# Create your models here.
class Book(models.Model):
    book_id=models.IntegerField()
    book_name=models.CharField(max_length=50)
    writer_name=models.CharField(max_length=50)

