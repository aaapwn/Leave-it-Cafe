from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'app_home/home.html')

def choose_one(request):
    return render(request, 'app_home/choose.html')
