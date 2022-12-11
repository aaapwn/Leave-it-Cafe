from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import write_your_post
from .models import Post

# Create your views here.
def board(request):
    all_post = Post.objects.order_by('-id')
    return render(request, 'app_postit/board.html', context = { 'all_post':all_post })

def postit(request, post_id):
    one_post = None
    try:
        one_post = Post.objects.get(id=post_id)
    except:
        pass
    return render(request, 'app_postit/postit.html', context={'post':one_post})

def writepost(request):
    if request.method == "POST":
        post = write_your_post(request.POST)
        if post.is_valid:
            post.save()
        return HttpResponseRedirect(reverse('board'))
    form = write_your_post
    return render(request, 'app_postit/writepost.html', context={'form':form})
