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


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'hakkimizda', 'category': category}
    return render(request, 'hakkimizda.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'referans', 'category': category}
    return render(request, 'references.html', context)


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


def category_hotels(request, id, slug):
    hotels = Hotel.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)

    context = {'hotels': hotels,
               'category': category,
               'slug': slug,
               'setting': setting,
               'categorydata': categorydata,

               }
    return render(request, 'hotels.html', context)


def hotel_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    rooms = Room.objects.filter(hotel_id=id)
    image = Images.objects.filter(hotel_id=id)
    hotel = Hotel.objects.get(pk=id)
    comments = Comment.objects.filter(hotel_id=id, status='True')
    context = {
        'hotel': hotel,
        'category': category,
        'image': image,
        'comments': comments,
        'rooms': rooms,
        'setting': setting,
    }
    return render(request, 'hotel_detail.html', context)


def hotel_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            hotel = Hotel.objects.filter(title__icontains=query)
            setting = Setting.objects.get(pk=1)

            context = {'hotel': hotel,
                       'category': category,

                       'setting': setting,

                       }
            return render(request, 'search_hotels.html', context)

    return HttpResponseRedirect('/')


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


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)

            user_profile = UserProfile()
            user_profile.user = user
            user_profile.image = "images/users/default.jpeg"
            user_profile.save()

            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'form': form,
        'setting': setting,
    }
    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    faq = FAQ.objects.all()
    context = {'category': category,
               'faq': faq,
               'setting': setting,
               }
    return render(request, 'faq.html', context)
