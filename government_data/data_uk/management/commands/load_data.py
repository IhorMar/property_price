from contextlib import closing
from itertools import islice
import requests
from django.core.management import BaseCommand

from data_uk.models import Price

property_type = {'D': 'Detached', 'S': 'Semi-Detached', 'T': 'Terraced', 'F': 'Flats/Maisonettes', 'O': 'Other'}
old_new_status = {'Y': 'a newly built property', 'N': 'an established residential building'}
duration_type = {'F': 'Freehold', 'L': 'Leasehold'}
category_type = {'A': "Standard Price Paid entry, includes single residential property sold for value.",
                 'B': "Additional Price Paid entry including transfers under a power of sale/repossessions, "
                      "buy-to-lets (where they"
                      "can be identified by a Mortgage), transfers to non-private individuals and sales where the "
                      "property type is"
                      "classed as ‘Other’."}
record_status = {'A': 'Addition',
                 'C': 'Change',
                 'D': 'Delete'}

fields_in_model = [
    'transaction_identifier', 'price', 'date_of_transfer', 'postcode', 'property_type', 'old_or_new', 'duration',
    'primary_addressable_object_name', 'secondary_addressable_object_name', 'property_street', 'property_locality',
    'property_city', 'property_district', 'property_country', 'type_price_paid_transaction', 'record_status']


def update_model(model, save_update=True, **kwargs):
    for attr, val in kwargs.items():
        if val in property_type:
            val = property_type[val]
            setattr(model, attr, val)
        if val in old_new_status:
            val = old_new_status[val]
            setattr(model, attr, val)
        if val in duration_type:
            val = duration_type[val]
            setattr(model, attr, val)
        if val in category_type:
            val = category_type[val]
            setattr(model, attr, val)
        if val in record_status:
            val = record_status[val]
            setattr(model, attr, val)
        else:
            setattr(model, attr, val)
    if save_update:
        model.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        Price.objects.all().delete()
        url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv"

        with closing(requests.get(url, stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            rows = list(islice(f, 100))
            for element in rows:
                element = element.replace('"', "")
                element = list(element.split(','))
                res = dict(zip(fields_in_model, element))
                price_data = Price()
                update_model(price_data, save_update=True, **res)
