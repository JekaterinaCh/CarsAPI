from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Cars
from .serializers import CarsSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def update_car(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    serializer = CarsSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_car(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
@ensure_csrf_cookie
def create_car(request):
    serializer = CarsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        car = Cars.objects.create(
            name=request.data['name'], year=request.data['year'])
        car.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cars_view(request, pk=None):
    if pk:
        car = get_object_or_404(Cars, pk=pk)
        serializer = CarsSerializer(car)
    else:
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
    return Response(serializer.data)

# susitvarkyt GET kad grazintu masyva su objektais ir kad rodytu ID, susitvarkyt delete taip pat kaip putss
    # POST, ATSISIUSTI POSTMAN, PUT, DELETE, GET
