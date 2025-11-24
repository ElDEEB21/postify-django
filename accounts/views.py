from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile
from blog.models import Post


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match.')
                return render(request, 'accounts/register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already registered.')
                return render(request, 'accounts/register.html', {'form': form})

            names = full_name.split(' ', 1)
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=names[0],
                last_name=names[1] if len(names) > 1 else ''
            )

            Profile.objects.create(user=user)

            auth_login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('profile')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    profile_obj, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if form.is_valid():
            profile = form.save(commit=False)

            # Handle avatar file upload
            avatar_file = form.cleaned_data.get('avatar_file')
            if avatar_file:
                # Read the file and store as binary
                profile.avatar = avatar_file.read()
                profile.avatar_type = avatar_file.content_type

            profile.save()

            name = form.cleaned_data.get("name")
            if name:
                names = name.split(" ", 1)
                request.user.first_name = names[0]
                request.user.last_name = names[1] if len(names) > 1 else ""
                request.user.save()

            return redirect("profile")
    else:
        initial_data = {"name": request.user.get_full_name()}
        form = ProfileForm(instance=profile_obj, initial=initial_data)
    
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')

    return render(request, "accounts/profile.html", {"form": form, "user_posts": user_posts})


def logout_view(request):
    auth_logout(request)
    return redirect("login")
