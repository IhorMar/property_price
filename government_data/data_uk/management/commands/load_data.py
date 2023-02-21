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


class Command(BaseCommand):
    def handle(self, *args, **options):
        Price.objects.all().delete()
        url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv"

        with closing(requests.get(url, stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            # reader = csv.reader(f, delimiter=',', quotechar='"')
            rows = list(islice(f, 100))
            for element in rows:
                price_data = Price()
                element = element.split(',')
                for _ in element:
                    price_data.transaction_identifier = element[0].strip('\"')
                    price_data.price = element[1].strip('\"')
                    price_data.date_of_transfer = element[2].strip('\"')
                    price_data.postcode = element[3].strip('\"')

                    if element[4].strip('\"') in property_type:
                        price_data.property_type = property_type[element[4].strip('\"')]
                    if element[5].strip('\"') in old_new_status:
                        price_data.old_or_new = old_new_status[element[5].strip('\"')]
                    if element[6].strip('\"') in duration_type:
                        price_data.duration = duration_type[element[6].strip('\"')]

                    price_data.primary_addressable_object_name = element[7].strip('\"')
                    price_data.secondary_addressable_object_name = element[8].strip('\"')
                    price_data.property_street = element[9].strip('\"')
                    price_data.property_locality = element[10].strip('\"')
                    price_data.property_city = element[11].strip('\"')
                    price_data.property_district = element[12].strip('\"')
                    price_data.property_country = element[13].strip('\"')

                    if element[14].strip('\"') in category_type:
                        price_data.type_price_paid_transaction = category_type[element[14].strip('\"')]

                    if element[15].strip('\"') in record_status:
                        price_data.record_status = record_status[element[15].strip('\"')]

                    price_data.save()
