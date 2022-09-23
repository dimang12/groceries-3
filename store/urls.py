from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views



# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductDetail.as_view()),
    path('categories/', views.category_list),
    path('category/<int:id>/', views.category_detail)
]