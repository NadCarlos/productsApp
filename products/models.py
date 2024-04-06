from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name