from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post_share/<int:pk>/', views.post_share, name='post_share'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
