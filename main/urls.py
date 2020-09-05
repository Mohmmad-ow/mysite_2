from django.urls import path
from .import views

urlpatterns = [
    path('to_do_lists/<int:id>', views.to_so_lists, name='to_do_list'),
    path('', views.index, name='index'),
    path('create/', views.create_form, name='create_form'),
    path('your_lists', views.user_tdl, name='user_todolist')
]