from django.shortcuts import render
from app.users.models import UserProfile
# Create your views here.


def home(request):
    context = {}
    if str(request.user) != 'AnonymousUser':
        user = request.user
        user = UserProfile.objects.get(user=user)
        context = {'user': user}
    else:
        user = "none"
        context = {'user': user}

    return render(request, "home.html", context)
