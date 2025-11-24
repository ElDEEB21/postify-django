from django import forms
from .models import Category, Tag


class BlogPostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Title',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your post title...'
        })
    )

    excerpt = forms.CharField(
        max_length=200,
        label='Excerpt',
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Write a brief summary of your post...',
            'rows': 3
        })
    )

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Write your post content here... (Supports Markdown)',
            'rows': 12
        })
    )

    cover_image = forms.ImageField(
        label='Cover Image',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-file-input',
            'accept': 'image/*'
        })
    )

    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        empty_label=None
    )

    tags = forms.ModelMultipleChoiceField(
        label='Tags',
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'tag-checkbox'
        }),
        required=False
    )
