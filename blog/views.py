from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from django.utils import timezone
from .forms import BlogPostForm
from .models import Post, Category, Tag


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()

        selected_category = self.request.GET.get('category')
        if selected_category:
            queryset = queryset.filter(category_id=selected_category)

        selected_tag = self.request.GET.get('tag')
        if selected_tag:
            queryset = queryset.filter(tags__id=selected_tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        context['selected_tag'] = self.request.GET.get('tag')
        context['all_categories'] = Category.objects.all()
        return context


def get_base_context(request):
    return {
        'all_categories': Category.objects.all()
    }


class WriteBlogView(LoginRequiredMixin, FormView):
    template_name = 'blog/write_blog.html'
    form_class = BlogPostForm
    login_url = 'login'

    def form_valid(self, form):
        post = Post(
            author=self.request.user,
            title=form.cleaned_data['title'],
            excerpt=form.cleaned_data['excerpt'],
            content=form.cleaned_data['content'],
            created_at=timezone.now(),
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

        return redirect('blog_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'message' in self.request.GET:
            context['message'] = 'Blog post created successfully!'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
