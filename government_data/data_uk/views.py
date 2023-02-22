from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from data_uk.models import Price
from .serializer import PriceSerializer


@api_view(['GET'])
def getPrice(request):
    price = Price.objects.all()
    serializer = PriceSerializer(price, many=True)
    return Response(serializer.data)
