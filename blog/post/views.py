from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    store=Post.objects.order_by('-date1')
    print(store)
    return render(request,'index.html',{'store':store})

def detail(request,id):
    obj=Post.objects.filter(pk=id)
    print(obj)
    return render(request,'detail.html',{'obj':obj})