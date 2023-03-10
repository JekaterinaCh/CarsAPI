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


@api_view(['GET', 'POST', 'DELETE'])
@renderer_classes([JSONRenderer])
def cars_list(request):
    if request.method == 'GET':
        return get_cars(request)
    elif request.method == 'POST':
        return create_car(request)
    elif request.method == 'DELETE':
        return delete_cars(request)


def get_cars(request):
    years = Cars.objects.values_list('year', flat=True).distinct()
    colors = Cars.objects.values_list('color', flat=True).distinct()
    year_from = request.GET.get('year_from')
    year_to = request.GET.get('year_to')
    color = request.GET.get('color')
    query = Cars.objects.all()
    if year_from is not None and year_from != '':
        query = query.filter(year__gte=year_from)
    if year_to is not None and year_to != '':
        query = query.filter(year__lte=year_to)
    if color is not None and color != '':
        query = query.filter(color=color)
    data = CarsSerializer(query, many=True).data
    return render(request, 'my_template.html', {'data': data, 'years': years, 'colors': colors})


def create_car(request):
    serializer = CarsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_cars(request):
    count = Cars.objects.all().delete()
    return Response({'message': '{} Cars were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@renderer_classes([JSONRenderer])
def cars_detail(request, pk):
    car = _get_car(pk)
    if car is None:
        return Response({'message': 'The car does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return _get_car_response(car)
    elif request.method == 'PUT':
        return _update_car_response(request, car)
    elif request.method == 'DELETE':
        return _delete_car_response(car)


def _get_car(pk):
    try:
        car = Cars.objects.get(pk=pk)
        return car
    except Cars.DoesNotExist:
        return None


def _get_car_response(car):
    car_serializer = CarsSerializer(car)
    return Response(car_serializer.data)


def _update_car_response(request, car):
    car_data = request.data
    car_serializer = CarsSerializer(car, data=car_data, partial=True)
    if car_serializer.is_valid():
        car_serializer.save()
        return Response(car_serializer.data)
    return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def _delete_car_response(car):
    car.delete()
    return Response({'message': 'Car was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# pasigalvoti laukus front endui, kaip django atvaizduoti lista objektu, atvaizduoti duomenis lenteles pavidalu ir virst lenteles filtrai ir su select funkcija (drop down) visiem laukam
