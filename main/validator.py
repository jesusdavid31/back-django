from django import forms

# from django.core.exceptions import ValidationError

# from main.models import User


class UserValidatorForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=3, required=True)
    surname = forms.CharField(max_length=50, min_length=3, required=True)
    nick = forms.CharField(max_length=70, min_length=3, required=True)
    email = forms.EmailField(required=True)
    bio = forms.CharField(max_length=500, required=False)
    password = forms.CharField(
        max_length=128, min_length=6, required=True, widget=forms.PasswordInput
    )
