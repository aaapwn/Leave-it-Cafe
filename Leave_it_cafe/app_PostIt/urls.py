from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:post_id>', views.postit, name='postit'),
]
