from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post
from .models import Comment
from .forms import CommentForm


def post_comments(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent=None).order_by('-created_at')
    form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'comment_count': post.comments.count()
    }
    
    return render(request, 'comments/comment_thread.html', context)


@login_required
def add_comment(request, slug, comment_id=None):
    post = get_object_or_404(Post, slug=slug)
    parent_comment = None
    
    if comment_id:
        parent_comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'POST':
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
    
    return redirect('post_comments', slug=slug)


@login_required
def delete_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, slug=slug)
    
    if request.user == comment.user or request.user == post.author:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this comment.')
    
    return redirect('post_comments', slug=slug)
