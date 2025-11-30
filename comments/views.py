from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from blog.models import Post
from .models import Comment
from .forms import CommentForm


class PostCommentsView(ListView):
    model = Comment
    template_name = 'comments/comment_thread.html'
    context_object_name = 'comments'
    
    def get_queryset(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return self.post.comments.filter(parent=None).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'post': self.post,
            'form': CommentForm(),
            'comment_count': self.post.comments.count()
        })
        return context


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, slug, comment_id=None):
        post = get_object_or_404(Post, slug=slug)
        parent_comment = None
        
        if comment_id:
            parent_comment = get_object_or_404(Comment, id=comment_id)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            
            message = 'Reply posted successfully!' if parent_comment else 'Comment posted successfully!'
            messages.success(request, message)
        
        return redirect('post_comments', slug=slug)
    
    def get(self, request, slug, comment_id=None):
        return redirect('post_comments', slug=slug)


class DeleteCommentView(LoginRequiredMixin, View):
    def post(self, request, slug, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post = get_object_or_404(Post, slug=slug)
        
        if request.user == comment.user or request.user == post.author:
            comment.delete()
            messages.success(request, 'Comment deleted successfully!')
        else:
            messages.error(request, 'You do not have permission to delete this comment.')
        
        return redirect('post_comments', slug=slug)
