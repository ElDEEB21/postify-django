from django.urls import path
from . import views
from core.views import HomePageView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('', HomePageView.as_view(), name='home')
]
