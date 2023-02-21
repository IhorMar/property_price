from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from data_uk.models import Price
from .serializer import PriceSerializer


# Create your views here.

@api_view(['GET'])
def getPrice(request):
    price = Price.objects.all()
    serializer = PriceSerializer(price, many=True)
    return Response(serializer.data)
# def get_data(request):
#     return HttpResponse("You're looking at question %s.---get_data")
#
#
# def data_detail(request):
#     return HttpResponse("You're looking at question %s.")
