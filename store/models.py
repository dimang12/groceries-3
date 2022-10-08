from datetime import datetime
from email.policy import default
from sqlite3 import Date
from datetime import date
from django.db import models

# Create your models here.
# class Categories(models.Model):
#     cateName = models.CharField(max_length=200)
#     cateDetail = models.TextField()
#     cateParent = models.IntegerField() 
#     cateCreated = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.cateName

# class Products(models.Model):
#     proName = models.CharField(max_length= 250)
#     categoryId = models.ForeignKey(Categories, on_delete= models.CASCADE)
#     proDetail = models.TextField()
#     proPrice = models.FloatField()
#     proWeight = models.CharField(max_length= 100)
#     proDimension = models.CharField(max_length= 200)
#     proIsPublish = models.BooleanField(default=True)
#     proCreated = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.proName

        
class Category(models.Model):
    cateName = models.CharField(max_length=200)
    cateDetail = models.TextField()
    cateParent = models.IntegerField() 
    cateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cateName

class Product(models.Model):
    proName = models.CharField(max_length= 250)
    categoryId = models.ForeignKey(Category, on_delete= models.CASCADE)
    proDetail = models.TextField(null=True)
    proPrice = models.FloatField(default=0.0)
    proWeight = models.CharField(max_length= 100, null=True)
    proDimension = models.CharField(max_length= 200, null=True)
    proIsPublish = models.BooleanField(default=True)
    proCreated = models.DateTimeField(auto_now_add=True)

    # Add new fields
    proAvailability = models.IntegerField(default=0)
    proOrigin = models.TextField(max_length=120, null=True)
    proProfile = models.TextField(null=True)
    proFacts = models.TextField(null=True)
    proStory = models.TextField(null=True)

    def __str__(self) -> str:
        return self.proName

class Review(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    reviewName = models.CharField(max_length=225, default='')
    reviewDescription = models.TextField(null=True, default='')
    reviewedDate = models.DateTimeField(default=datetime.today)
