from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'home/index.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'home/dashboard.html')


@login_required(login_url='/accounts/login/')
def category(request):
    return render(request, 'category/index.html')

@login_required(login_url='/accounts/login/')
def create_category(request):
    return render(request, 'category/create.html')

@login_required(login_url='/accounts/login/')
def brand(request):
    return render(request, 'brand/index.html')

@login_required(login_url='/accounts/login/')
def create_brand(request):
    return render(request, 'brand/create.html')

def login(request):
    return render(request, 'home/login.html')


def create(request):
    return render(request, 'home/create.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
