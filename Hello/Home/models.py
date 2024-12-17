from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    Phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
