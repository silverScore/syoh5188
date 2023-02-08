from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ExtendedUserForm


# class SignupForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = ExtendedUserForm
#         fields = ['username', 'password', 'email', 'phone', 'created_at']


# class ChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = ExtendedUserForm
#         fields = ['username', 'password', 'email', 'phone', 'created_at']
