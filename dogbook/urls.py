"""dogbook URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import app.temptest.views
import app.users.views
import app.users.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cards/', include('app.cards.urls')),
    url(r'^users/', include('app.users.urls')),
    url(r'^comments/', include('app.comments.urls')),
    url(r'^likes/', include('app.likes.urls')),
    url(r'^$', app.temptest.views.home, name="home"),
    url(r'^about/$', app.users.views.about, name="about"),
    url(r'^contact/$', app.users.views.contact, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
