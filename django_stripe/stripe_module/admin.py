from django.contrib import admin
from .models import Item, StripeProductApi, Order

admin.site.register(Item)
admin.site.register(StripeProductApi)
admin.site.register(Order)
