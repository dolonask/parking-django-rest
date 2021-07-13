import math

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tariff, Operation
from .serializers import TariffSerializer, OperationSerializer

from .services import tariff_detail

from datetime import  datetime

from .services.tariff_detail import get_amount_to_pay


@api_view(['GET', 'POST'])
def tariff(request):

    if request.method == 'GET':
        list = Tariff.objects.all()
        serializer = TariffSerializer(list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        t = request.data
        serializer = TariffSerializer(data=t)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def operation(request):

    if request.method == 'POST':
        operation = request.data
        serializer = OperationSerializer(data=operation)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def close_operation(request, pk):
    if request.method == 'GET':
        operation = Operation.objects.get(pk = pk)

        amount_to_pay = get_amount_to_pay(operation)
        return Response({"amount_to_pay": amount_to_pay})
        # details = tariff_detail.get_curr_tariff_details()
        #
        # start_date = operation.start_date
        # end_date = datetime.now()
        #
        # period = (end_date - start_date).seconds / 60 / 60
        #
        # for detail in details:
        #     if period < detail.hours:
        #         price = math.ceil(period) * detail.price







