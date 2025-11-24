from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import BlogPostForm
from .models import Post, Category, Tag


def blog_home(request):
    return render(request, 'blog/blog_home.html')


@login_required
def write_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                author=request.user,
                title=form.cleaned_data['title'],
                excerpt=form.cleaned_data['excerpt'],
                content=form.cleaned_data['content'],
                created_at=timezone.now()
            )

            cover_image_file = form.cleaned_data.get('cover_image')
            if cover_image_file:
                post.cover_image = cover_image_file.read()
                post.cover_image_type = cover_image_file.content_type
                
            post.category = form.cleaned_data.get('category')
            
            post.save()

            selected_tags = form.cleaned_data.get('tags')
            if selected_tags:
                post.tags.set(selected_tags)

            return render(request, 'blog/blog_home.html', {'message': 'Blog post created successfully!'})
    else:
        form = BlogPostForm()

    return render(request, 'blog/write_blog.html', {'form': form})
