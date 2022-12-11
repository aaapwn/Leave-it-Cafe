from django.urls import path
from . import views

urlpatterns = [
    path('', views.cafe, name='cafe'),
    path('send', views.send, name='send'),
    path('getmessages', views.getmessage, name='getmessage')
]
