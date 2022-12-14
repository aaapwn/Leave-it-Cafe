from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from app_home.models import Profile
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

# Create your views here.
@login_required
def cafe(request):
    user = request.user
    try:
        username = Profile.objects.get(user=user).displayname
    except:
        username = "Unknown"
    return render(request, 'app_cafe/cafe.html', context={'displayname':username})

def send(request):
    try:
        displayname = request.POST['displayname']
    except:
        displayname = "Unknown"
    message = request.POST['message']
    print(displayname)
    new_message = Message.objects.create(text=message, displayname=displayname)
    new_message.save()
    return HttpResponse("SEND!!!")

def getmessage(request):
    messages = Message.objects.all()
    print(messages)
    return JsonResponse({"messages":list(messages.values())})
