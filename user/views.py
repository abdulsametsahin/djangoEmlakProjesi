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


@login_required(login_url='/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profilin başarıyla güncellendi!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(
            instance=request.user.userprofile)  # "userprofile" model -> OneToOneField relatinon with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'setting': setting,
        }
        return render(request, 'user_update.html', context)