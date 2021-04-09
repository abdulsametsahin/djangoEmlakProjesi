from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormMessage, FAQ, ContactForm
from hotel.models import *
from user.models import *


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Hotel.objects.all()[:4]
    fivestarhotels = Hotel.objects.filter(star='5')[:]
    lasthotels = Hotel.objects.all().order_by('-id')[:6]
    randomhotels = Hotel.objects.all().order_by('?')[:6]
    specialhotels = Hotel.objects.filter(city='Antalya')[:]
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'fivestarhotels': fivestarhotels,
               'lasthotels': lasthotels,
               'randomhotels': randomhotels,
               'specialhotels': specialhotels
               }
    return render(request, 'index.html', context)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarılı ile gönderilmiştir. Teşekkür Ederiz ")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş başarısız. Tekrar Deneyiniz.")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request, 'login.html', context)
