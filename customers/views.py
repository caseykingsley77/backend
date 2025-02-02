from . models import * 
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['Get', 'POST'])
def customers(request):
    if request.method == 'GET':
        data = Customer.objects.all()
        serializer = CustomerSerialzer(data, many= True)
        return Response({'customers': serializer.data})
    elif request.method == 'POST':
        serializer = CustomerSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer' : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# this view runs the crud func    
@api_view(['Get', 'POST', 'DELETE'])
def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerialzer(data)
        return Response({'customer': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = CustomerSerialzer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
