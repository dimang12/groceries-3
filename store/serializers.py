from dataclasses import field, fields
from operator import mod
from pyexpat import model
from rest_framework import serializers
from store.models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "cateName", "productsCount"]
    
    productsCount = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "categoryId", "proName", "proDetail", "proPrice", "priceWithTax"]

    priceWithTax = serializers.SerializerMethodField(method_name='calculateTax')

    def calculateTax (self, product: Product):
        return product.proPrice * 1.1
    
    # Create new Product
    def create(self, validate_data):
        product = Product(**validate_data)
        product.other = 1
        product.save()
        return product

    #Update an existing Product
    def update(self, instance, validate_data):
        instance.proName = validate_data.get('proName')
        instance.save()
        return instance

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'reviewName', 'reviewDescription', 'productId', 'reviewedDate']