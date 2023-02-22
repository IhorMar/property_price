from .models import Price


def get_search_fields(model):
    """ Defines what the list page search box of the admin page queries to get its results """

    PriceFilter = Price
    dic = {
        PriceFilter: ['property_type', 'date_of_transfer', 'property_locality', 'old_or_new'],
    }
    return dic.get(model,)
