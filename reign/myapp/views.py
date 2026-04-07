from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.

def user_list(request):
    records=User.objects.all()
    mydict={'records':records}