from django.contrib import admin
from .models import Products, City, Region, Favorited


admin.site.register(Products)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Favorited)