from django.contrib import admin

from .models import Event, Order, Product, Team

admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Order)
admin.site.register(Product)
