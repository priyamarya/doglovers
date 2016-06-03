from django.shortcuts import render
from app.users.models import UserProfile
# Create your views here.


def home(request):
    
    return render(request, "home.html", {})
