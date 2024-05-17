# blog/urls.py
from django.urls import path

from FirstApp import views
# from FirstApp.views import home, post_detail
# from views import home, post_detail
# Import these functions from views.py

urlpatterns = [
    path('', views.home),
    path('FirstApp/<int:post_id>', views.post_detail, name="post_detail"),
]