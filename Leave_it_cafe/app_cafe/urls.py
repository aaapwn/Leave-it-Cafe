from django.urls import path
from . import views

urlpatterns = [
    path('', views.cafe, name='cafe'),
    path('entername', views.enter_name, name='cafe')
]
