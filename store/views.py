from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

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
        serializer.validated_data
        return Response('It is valid')
        

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        proDict = ProductSerializer(product) 
        return Response(proDict.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

