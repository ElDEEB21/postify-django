from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='blog_home'),
    path('write/', views.WriteBlogView.as_view(), name='write_blog'),
    path('edit/<str:slug>/', views.WriteBlogView.as_view(), name='edit_blog'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
