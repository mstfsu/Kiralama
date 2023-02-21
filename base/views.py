from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)