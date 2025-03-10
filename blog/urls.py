from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post_share/<int:pk>/', views.post_share, name='post_share'),
]
