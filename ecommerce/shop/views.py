from django.shortcuts import render
from django.views import View
from shop.models import Category

# Create your views here
class Categories(View):
    def get(self,request):
        c=Category.objects.all()
        context={'categories':c}
        return render(request,'category.html',context)

class Product(View):
    def get(self,request,i):
        c=Category.objects.get(id=i)
        context={'categories':c}
        return render(request,'products.html',context)
