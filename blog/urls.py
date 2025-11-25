from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('write/', views.write_blog, name='write_blog'),
    path('<str:slug>/', views.post_detail, name='post_detail'),
]