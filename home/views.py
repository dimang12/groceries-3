import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product

# Create your views here.
def index(request):
    # return query set not dataset
    queryset = Product.objects.all()

    try:
        getProduct = Product.objects.get(pk=1)
        # getProduct = Product.objects.filter(pk=1).first()
    except ObjectDoesNotExist:
        pass


    print(getProduct)
   
    return render(request, 'home.html')
