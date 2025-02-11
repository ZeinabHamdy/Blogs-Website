from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:page_needed>/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
]
