from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')

def login(request):
    return render(request, 'home/login.html')

def create(request):
    return render(request, 'home/create.html')

def logout_view(request):
    logout(request)