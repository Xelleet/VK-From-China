from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('user/<int:index>', views.userprofile, name='userprofile'),
    path('add_post/<int:index>', views.add_post, name='add_post'),
    path('delete_post/<int:index>', views.delete_post, name='delete_post'),
    path('add_friend/<int:index>', views.add_friend, name='add_friend')
]