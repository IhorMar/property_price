from django.contrib.admin import ModelAdmin
from data_uk.admin_utils import get_search_fields
from data_uk.models import Price


class PriceAdmin(ModelAdmin):
    fields = (
        'transaction_identifier', 'price', 'date_of_transfer', 'postcode', 'property_type', 'old_or_new', 'duration',
        'primary_addressable_object_name', 'secondary_addressable_object_name', 'property_street', 'property_locality',
        'property_city', 'property_district', 'property_country', 'type_price_paid_transaction', 'record_status')
    list_display = ('property_type', 'date_of_transfer', 'property_locality', 'old_or_new')
    readonly_fields = ('transaction_identifier',)
    ordering = ('-date_of_transfer',)
    list_per_page = 40
    search_fields = get_search_fields(Price)
    list_filter = ('old_or_new',)
