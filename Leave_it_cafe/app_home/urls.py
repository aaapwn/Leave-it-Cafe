from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('choose-one', views.choose_one, name='choose-one'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/registeration', views.register, name='register'),
    path('user/profile', views.profile, name='profile'),
]
