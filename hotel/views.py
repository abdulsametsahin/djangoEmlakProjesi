from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from hotel.models import CommentForm, Comment


def index(request):
    return HttpResponse("Hotel Page")

