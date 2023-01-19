from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/cars/', views.cars_view),
    path('api/cars/create/', views.create_car),
]
