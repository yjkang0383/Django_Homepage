from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/blog
    path('', views.post_list, name='post_list_home'),
    # http://localhost:8000/blog/post/5
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]