from django.conf.urls import url
from .views import login, register, logout, user_details_entry1, user


urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="signup"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^userdetailsentry/$', user_details_entry1, name="details"),
    url(r'^(?P<username>\w+)$', user),



]
