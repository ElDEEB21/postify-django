from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, View, UpdateView
from django.urls import reverse
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile
from blog.models import Post
from comments.models import Comment


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user_profile', username=request.user.username)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if password != confirm_password:
            form.add_error('confirm_password', 'Passwords do not match.')
            return self.form_invalid(form)

        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Email already registered.')
            return self.form_invalid(form)

        names = full_name.split(' ', 1)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=names[0],
            last_name=names[1] if len(names) > 1 else ''
        )

        Profile.objects.create(user=user)
        auth_login(self.request, user,
                   backend='django.contrib.auth.backends.ModelBackend')
        return redirect('user_profile', username=user.username)


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user_profile', username=request.user.username)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            auth_login(self.request, user)
            return redirect('user_profile', username=user.username)
        else:
            form.add_error(None, 'Invalid email or password.')
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect('login')


class UserProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        profile_user = get_object_or_404(User, username=username)
        profile_obj, created = Profile.objects.get_or_create(user=profile_user)
        return profile_obj

    def get_profile_user(self):
        """Cache and return the profile user."""
        if not hasattr(self, '_profile_user'):
            username = self.kwargs.get('username')
            self._profile_user = get_object_or_404(User, username=username)
        return self._profile_user

    def is_own_profile(self):
        """Check if the current user is viewing their own profile."""
        return (self.request.user.is_authenticated and 
                self.request.user.username == self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.get_profile_user()

        context.update({
            'profile_user': profile_user,
            'profile': self.get_object(),
            'user_posts': Post.objects.filter(author=profile_user).order_by('-created_at'),
            'is_own_profile': self.is_own_profile(),
            'comment_count': Comment.objects.filter(user=profile_user).count(),
            'views_count': sum(post.views for post in Post.objects.filter(author=profile_user).order_by('-created_at'))
        })
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile_user = self.get_profile_user()
        kwargs['initial'] = {'name': profile_user.get_full_name()}
        return kwargs

    def form_valid(self, form):
        if not self.is_own_profile():
            return redirect('user_profile', username=self.kwargs.get('username'))

        profile = form.save(commit=False)
        avatar_file = form.cleaned_data.get('avatar_file')

        if avatar_file:
            profile.avatar = avatar_file.read()
            profile.avatar_type = avatar_file.content_type

        profile.save()

        name = form.cleaned_data.get('name')
        if name:
            names = name.split(' ', 1)
            self.request.user.first_name = names[0]
            self.request.user.last_name = names[1] if len(names) > 1 else ''
            self.request.user.save()

        return redirect('user_profile', username=self.kwargs.get('username'))

    def post(self, request, *args, **kwargs):
        if not self.is_own_profile():
            return redirect('user_profile', username=self.kwargs.get('username'))
        return super().post(request, *args, **kwargs)
