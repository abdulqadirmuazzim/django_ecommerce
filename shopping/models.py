from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField as PNF


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = PNF()
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
