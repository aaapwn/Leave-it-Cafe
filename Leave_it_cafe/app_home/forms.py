from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, CustomUSer

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUSer
        fields = UserCreationForm.Meta.fields + ('email', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUSer
        fields = ("email", )

class ExtendedProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("displayname", )
