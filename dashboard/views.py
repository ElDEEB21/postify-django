from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from blog.models import Post
from comments.models import Comment
from django.utils import timezone
from datetime import timedelta
import calendar


class DashboardHomeView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request):
        user = request.user
        
        total_posts = Post.objects.filter(author=user, is_archived=False).count()
        archived_posts = Post.objects.filter(author=user, is_archived=True).count()
        total_comments = Comment.objects.filter(post__author=user).count()
        total_views = sum(post.views for post in Post.objects.filter(author=user, is_archived=False))
        
        recent_posts = Post.objects.filter(author=user).order_by('-created_at')[:5]
        
        now = timezone.now()
        monthly_data = []
        
        for i in range(11, -1, -1):
            month_date = now - timedelta(days=30 * i)
            month_start = month_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            if month_date.month == 12:
                month_end = month_start.replace(year=month_start.year + 1, month=1)
            else:
                month_end = month_start.replace(month=month_start.month + 1)
            
            count = Post.objects.filter(
                author=user,
                created_at__gte=month_start,
                created_at__lt=month_end
            ).count()
            
            monthly_data.append({
                'month': calendar.month_abbr[month_start.month],
                'count': count
            })
        
        context = {
            'total_posts': total_posts,
            'archived_posts': archived_posts,
            'total_comments': total_comments,
            'total_views': total_views,
            'recent_posts': recent_posts,
            'monthly_data': monthly_data,
        }
        
        return render(request, 'dashboard/dashboard_home.html', context)
    