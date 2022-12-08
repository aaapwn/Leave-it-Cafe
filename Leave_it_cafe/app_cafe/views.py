from django.shortcuts import render

# Create your views here.
def cafe(request):
    return render(request, 'app_cafe/cafe.html')
