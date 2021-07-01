from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting
from hotel.models import Hotel, Room
from reserve.models import ReserveForm, Reserve


def index(request):
    return HttpResponse("Reserve Page")



@login_required(login_url="/login")
def sendreserve(request,id,hotel_id):
    url = request.META.get('HTTP_REFERER')  # get last url
    hotel = Hotel.objects.get(id=hotel_id)
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = ReserveForm(request.POST)
        if form.is_valid():
            data = Reserve()  # create relation with model
            data.hotel_id = hotel.id
            data.room_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.checkin = form.cleaned_data['checkin']
            data.checkout = form.cleaned_data['checkout']
            data.save()  # save data to table
            messages.success(request, "Rezervasyonunuz Alınmıştır. Teşekkür ederiz.")
            return HttpResponseRedirect('/user/reserve')

    return HttpResponseRedirect(url)