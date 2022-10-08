
import imp
from itertools import count
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from store.filters import ProductFilter
from store.pagination import DefaultPagination

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['proName', 'proDetail']
    ordering_fields = ['proName', 'proPrice']
    
    

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     categoryId = self.request.query_params.get('categoryId')
        
    #     if categoryId is not None:
    #         queryset = queryset.filter(categoryId=categoryId)
    #     return queryset

    def get_serializer_context(self):
        return {'request': self.request}


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(productsCount=Count('product')).all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(categoryId = kwargs['pk']).count() > 0:
            return Response({'error': 'Category cannot be deleted'})
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class ProductList(APIView):
# class ProductList(ListCreateAPIView):
#     def get_queryset(self):
#         return Product.objects.select_related('categoryId').all()

#     def get_serializer_class(self):
#         return ProductSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}

    # def get(self, request):
    #     querySet = Product.objects.select_related('categoryId').all()
    #     serializerProducts = ProductSerializer(querySet, many = True)
    #     return Response(serializerProducts.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     serializer.validated_data
    #     return Response(serializer.data, status= status.HTTP_201_CREATED)

# class ProductDetail(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk = pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.annotate(productsCount=Count('product')).all()
#     serializer_class = CategorySerializer

# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.annotate(productsCount=Count('product')).all()
#     serializer_class = CategorySerializer

#     def delete(self, request, pk):
#         category = Category.objects.annotate(productsCount=Count('product')).get(pk=pk)

#         # print(category.productsCount)
#         if category.productsCount > 0:
#             return Response({'error': 'Category cannot be deleted'})

        
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         querySet = Category.objects.annotate(productsCount=Count('product')).all()
#         serializer = CategorySerializer(querySet, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         category = get_object_or_404(Category, pk = id)
#         serializer = CategorySerializer(category, data= request.data)
#         serializer.save()
#         return Response('Saved')


# @api_view(['GET','PUT'])
# def category_detail(request, id):
#     category = get_object_or_404(Category, pk=id)
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response('Saved')
