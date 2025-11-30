from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.post_comments, name='post_comments'),
    path('<slug:slug>/add/', views.add_comment, name='add_comment'),
    path('<slug:slug>/reply/<int:comment_id>/', views.add_comment, name='add_reply'),
    path('<slug:slug>/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
