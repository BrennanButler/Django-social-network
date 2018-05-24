from authentication.models import User
from django import forms

# TODO: Find a way to reference the User model through settings


class UserCreate(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# TODO: Make a custom form in which the user can login with either their username or email
class UserLogin(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']
