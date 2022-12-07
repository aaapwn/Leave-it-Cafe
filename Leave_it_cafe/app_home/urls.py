from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('choose-one', views.choose_one, name='choose-one'),
]
