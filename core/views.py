from django.views.generic import TemplateView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.all().order_by(
            '-created_at')[:3]
        context['latest_posts'] = Post.objects.all().order_by(
            '-created_at')[:6]
        return context


class AboutPageView(TemplateView):
    template_name = 'core/about.html'


class ContactPageView(TemplateView):
    template_name = 'core/contact.html'
