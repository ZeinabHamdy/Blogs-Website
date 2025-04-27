from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post_share/<int:pk>/', views.post_share, name='post_share'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('person_posts/<int:pk>/', views.person_posts, name='person_posts'),
]
