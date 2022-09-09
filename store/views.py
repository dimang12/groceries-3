from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
    if(request.method == 'GET'):
        querySet = Product.objects.select_related('categoryId').all()
        serializerProducts = ProductSerializer(querySet, many = True)
        return Response(serializerProducts.data)
    elif(request.method == 'POST'):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status= status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk = id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        querySet = Category.objects.all()
        serializer = CategorySerializer(querySet, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response('Saved')
