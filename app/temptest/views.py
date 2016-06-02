from django.shortcuts import render
from app.users.models import UserProfile
# Create your views here.


def home(request):
    user = request.user
    user = UserProfile.objects.get(user=user)
    context = {'user': user}
    return render(request, "home.html", context)
