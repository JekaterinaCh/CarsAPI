from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import CarsSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


@api_view(['POST'])
@renderer_classes([JSONRenderer])
@ensure_csrf_cookie
def create_car(request):
    print(request)
    serializer = CarsSerializer(data={'name': 'BMW', 'year': 2022})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def cars_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, year FROM Cars")
        rows = cursor.fetchall()
    data = {'cars': rows}
    return JsonResponse(data)

    # POST, ATSISIUSTI POSTMAN, PUT, DELETE, GET
