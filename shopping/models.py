from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15, help_text="Enter phone e.g +1 123-456-7980")
    message = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class product(models.Model):
    Pname = models.CharField(max_length=50)
    image = models.URLField(max_length=500)
    price = models.IntegerField()
