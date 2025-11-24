from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Sarah Johnson'
        })
    )

    avatar_file = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-input',
            'accept': 'image/*'
        }),
        label='Profile Picture'
    )

    class Meta:
        model = Profile
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Tech writer and software developer. Passionate about web development and design.',
                'rows': 4
            })
        }
        labels = {
            'bio': 'Bio'
        }


class RegisterForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'John Doe',
            'id': 'full_name'
        }),
        error_messages={
            'max_length': 'Full name cannot exceed 100 characters.',
            'required': 'Please enter your full name.',
            'min_length': 'Full name must be at least 2 characters long.'
        }
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'your@email.com',
            'id': 'email'
        }),
        error_messages={
            'invalid': 'Enter a valid email address.',
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '********',
            'id': 'password'
        }),
        error_messages={
            'required': 'Please enter your password.',
        }
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '********',
            'id': 'confirm_password'
        }),
        error_messages={
            'required': 'Please confirm your password.',
        }
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'your@email.com',
            'id': 'email'
        }),
        error_messages={
            'invalid': 'Enter a valid email address.',
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '********',
            'id': 'password'
        }),
        error_messages={
            'required': 'Please enter your password.',
        }
    )
