from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting
from hotel.models import Category
from reserve.models import Reserve
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    profile = UserProfile.objects.get(user_id=request.user.id)
    context = {
        'setting': setting,
        'category': category,
        'profile': profile,

    }
    return render(request, 'user_profile.html', context)


