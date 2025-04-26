from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post_share/<int:pk>/', views.post_share, name='post_share'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
]
