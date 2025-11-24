from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import BlogPostForm
from .models import Post, Category, Tag


def blog_home(request):
    posts = Post.objects.all().order_by('-created_at')
    total_posts = posts.count()

    selected_category = request.GET.get('category')
    if selected_category:
        posts = posts.filter(category_id=selected_category)
    
    selected_tag = request.GET.get('tag')
    if selected_tag:
        posts = posts.filter(tags__id=selected_tag)
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'posts': posts,
        'total_posts': total_posts,
        'categories': categories,
        'tags': tags,
        'selected_category': selected_category,
        'selected_tag': selected_tag,
        'all_categories': categories,
    }
    
    return render(request, 'blog/blog_home.html', context)


def get_base_context(request):
    return {
        'all_categories': Category.objects.all()
    }


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
