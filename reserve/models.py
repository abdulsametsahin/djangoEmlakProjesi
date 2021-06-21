from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.forms import ModelForm

from hotel.models import Room, Hotel


class Reserve(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Onaylandı', 'Onaylandı'),
        ('Reddedildi', 'Reddedildi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = ['checkin', 'checkout']

    def __str__(self):
        return self.hotel
