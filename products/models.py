from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=30)
    ref = models.CharField(max_length=20, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    salesprice = models.FloatField(blank=True, default=0, null=True)
    buyprice = models.FloatField(default=0, null=True, blank=True)
    quantity = models.FloatField(default=0, null=True)
    sales_comission = models.FloatField(blank=True, default=0, null=True)
    bonus = models.FloatField(default=0, null=True, blank=True)
    package_cost = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

