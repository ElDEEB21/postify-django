from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, View, UpdateView
from django.urls import reverse
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile
from blog.models import Post


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        profile_user = get_object_or_404(User, username=username)

        context['profile_user'] = profile_user
        context['profile'] = self.get_object()
        context['user_posts'] = Post.objects.filter(
            author=profile_user).order_by('-created_at')
        context['is_own_profile'] = self.request.user.is_authenticated and self.request.user.username == username
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile_user = get_object_or_404(
            User, username=self.kwargs.get('username'))
        kwargs['initial'] = {'name': profile_user.get_full_name()}
        return kwargs

    def form_valid(self, form):
        is_own_profile = self.request.user.is_authenticated and self.request.user.username == self.kwargs.get(
            'username')

        if not is_own_profile:
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
        is_own_profile = request.user.is_authenticated and request.user.username == self.kwargs.get(
            'username')
        if not is_own_profile:
            return redirect('user_profile', username=self.kwargs.get('username'))
        return super().post(request, *args, **kwargs)
