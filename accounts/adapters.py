from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import User


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)

        if not user.username and user.email:
            base_username = user.email.split('@')[0]
            username = base_username
            counter = 1

            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1

            user.username = username

        if commit:
            user.save()
        return user


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        if not user.username and user.email:
            base_username = user.email.split('@')[0]
            username = base_username
            counter = 1

            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1

            user.username = username

        return user
