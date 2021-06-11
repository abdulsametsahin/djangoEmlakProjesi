from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('reserve/', views.reserve, name='reserve'),
    path('reservedelete/<int:id>', views.reservedelete, name='reservedelete'),
]
