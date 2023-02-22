from django.contrib import admin

from data_uk.models import Price
from data_uk.price_admin.price import PriceAdmin

# Register your models here.
admin.site.register(Price, PriceAdmin)
