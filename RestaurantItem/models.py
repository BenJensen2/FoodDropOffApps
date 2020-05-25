from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)