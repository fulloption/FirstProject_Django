# Register your models here.
# blog/admin.py
from django.contrib import admin
from FirstApp.models.Post import Post

admin.site.register(Post)