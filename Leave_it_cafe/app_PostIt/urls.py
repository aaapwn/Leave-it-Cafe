from django.urls import path
from . import views
urlpatterns = [
    path('', views.board, name='board'),
    path('<int:post_id>', views.postit, name='postit'),
    path('write_your_post', views.writepost, name='writepost'),
]
