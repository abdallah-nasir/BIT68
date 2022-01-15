from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product (models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
