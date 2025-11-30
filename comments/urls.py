from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.PostCommentsView.as_view(), name='post_comments'),
    path('<slug:slug>/add/', views.AddCommentView.as_view(), name='add_comment'),
    path('<slug:slug>/reply/<int:comment_id>/', views.AddCommentView.as_view(), name='add_reply'),
    path('<slug:slug>/delete/<int:comment_id>/', views.DeleteCommentView.as_view(), name='delete_comment'),
]
