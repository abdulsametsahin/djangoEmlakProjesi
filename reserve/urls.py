from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendreserve/<int:id>/<int:hotel_id>', views.sendreserve, name='sendreserve'),

]
