# blog/views.py
from django.shortcuts import render
from FirstApp.models.Post import Post

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