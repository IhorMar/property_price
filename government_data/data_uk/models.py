from django.db import models

# Create your models here.


class Price(models.Model):
    transaction_identifier = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=100, blank=True)
    date_of_transfer = models.DateTimeField()
    postcode = models.CharField(max_length=100, blank=True)
    property_type = models.CharField(max_length=100, blank=True)
    old_or_new = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    primary_addressable_object_name = models.CharField(max_length=100, blank=True)
    secondary_addressable_object_name = models.CharField(max_length=100, blank=True)
    property_street = models.CharField(max_length=200, blank=True)
    property_locality = models.CharField(max_length=200, blank=True)
    property_city = models.CharField(max_length=200, blank=True)
    property_district = models.CharField(max_length=200, blank=True)
    property_country = models.CharField(max_length=200, blank=True)
    type_price_paid_transaction = models.CharField(max_length=100, blank=True)
    record_status = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"

    def __str__(self):
        return self.transaction_identifier
    # Transaction unique identifier
    # Price
    # Date of Transfer
    # Postcode
    # Property Type
    # Old / New
    # Duration
    # PAON
    # SAON
    # Street
    # Locality
    # Town / City
    # District
    # County
    # PPD Category Type
    # Record Status - monthly file only