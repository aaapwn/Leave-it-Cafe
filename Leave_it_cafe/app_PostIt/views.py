from django.shortcuts import render

data = [
    {'id':1, 'to':'A.', 'text':'สวัสดีจ้า', 'from':'ff'},
    {'id':2, 'to':'Z', 'text':"HI JA", 'from':'bb'},
    {'id':3, 'to':'Ayu', 'text':'secret', 'from':'ee'}
]

# Create your views here.
def board(request):
    context = { 'all_post':data }
    return render(request, 'app_postit/board.html', context)

def postit(request, post_id):
    one_post = None
    try:
        one_post = [post for post in data if post['id'] == post_id][0]
    except:
        pass
    return render(request, 'app_postit/postit.html', context={ 'post':one_post })
