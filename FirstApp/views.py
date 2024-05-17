# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'FirstApp/home.html', {
        'posts': posts
    })

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'FirstApp/post-detail.html', {
        'post': post
    })