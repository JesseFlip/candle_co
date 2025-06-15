from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    if request.methon == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
    return render(request, "users/login.html")

def logout_view(request):
    pass
    #return render(request, "users/logout.html")