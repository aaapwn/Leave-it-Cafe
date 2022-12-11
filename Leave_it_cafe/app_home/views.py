from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse
from .forms import UserProfileForm, ExtendedProfileForm
from .models import Profile
from django.core.exceptions import PermissionDenied
from django.contrib import admin
# Create your views here.
def main(request):
    """homepage"""
    return render(request, 'app_home/home.html')

def choose_one(request):
    """select cafe or board"""
    return render(request, 'app_home/choose.html')

def register(request: HttpRequest):
    """registeration"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(request.POST)
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm
    return render(request, 'app_home/register.html', context={'form':form})

@login_required
def profile(request: HttpRequest):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False

        try:
            extend = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            extend = ExtendedProfileForm(request.POST)
            is_new_profile = True
        if form.is_valid() and extend.is_valid():
            form.save()
            if is_new_profile:
                profile = extend.save(commit=False)
                profile.user = user
                profile.save()
            else:
                extend.save()
            response = HttpResponseRedirect(reverse('profile'))
            response.set_cookie("is_saved", "1")
            return response
    else:
        form = UserProfileForm(instance=user)
        try:
            extend = ExtendedProfileForm(instance=user.profile)
        except:
            extend = ExtendedProfileForm()
    is_saved = request.COOKIES.get("is_saved") == "1"
    flash_message = "บันทึกข้อมูลเรียบร้อย" if is_saved else None
    context = {
        'form' : form,
        'extend' : extend,
        'flash_message' : flash_message
    }
    response = render(request, 'app_home/profile.html', context)
    if is_saved:
        response.delete_cookie("is_saved")
    return response

