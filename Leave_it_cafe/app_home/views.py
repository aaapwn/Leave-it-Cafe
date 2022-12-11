from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse

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
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm
    return render(request, 'app_home/register.html', context={'form':form})
