from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate


class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if not confirm_password:
            raise forms.ValidationError("You must confirm your password")
        if password != confirm_password:
            raise forms.ValidationError("Password do not match")
        return confirm_password

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry,")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


UserCreationFormset = inlineformset_factory(
    User, UserProfile, can_delete=False, exclude=['points', 'social_media',
                                                  'messages', 'img_height', 'img_width'])
