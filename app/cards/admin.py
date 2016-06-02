from django.contrib import admin
from .models import Cards
# Register your models here.


class CardsAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'user']

admin.site.register(Cards, CardsAdmin)
