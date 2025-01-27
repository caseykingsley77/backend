from . models import * 
from django.http import JsonResponse
from customers.serializers import CustomerSerialzer


def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerialzer(data, many= True)
    return JsonResponse({'customers': serializer.data})