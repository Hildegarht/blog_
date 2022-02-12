from django.shortcuts import render
from .models import Post

def home(request,hm):
    posts = Post.objects.get(id='hm')
    return render(request,'home.html',{'posts':posts})

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'post.html',{'posts':posts})
# Create your views here.
