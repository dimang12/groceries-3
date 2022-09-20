import imp
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class ProductList(APIView):
    def get(self, request):
        querySet = Product.objects.select_related('categoryId').all()
        serializerProducts = ProductSerializer(querySet, many = True)
        return Response(serializerProducts.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status= status.HTTP_201_CREATED)

class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk = id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=1)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=1)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        querySet = Category.objects.all()
        serializer = CategorySerializer(querySet, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        category = get_object_or_404(Category, pk = id)
        serializer = CategorySerializer(category, data= request.data)
        serializer.save()
        return Response('Saved')

@api_view(['GET','PUT'])
def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Saved')
