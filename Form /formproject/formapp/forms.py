from django import forms
from django.contrib.auth.models import User
from .models import Post


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')






class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
