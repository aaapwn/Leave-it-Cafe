from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, CustomUSer

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Username', 'class':'typebox'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your E-mail', 'class':'typebox'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password', 'class':'typebox'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm your Password', 'class':'typebox'}))
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

