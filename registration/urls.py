from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/cars/', views.cars_view),
    path('api/cars/create/', views.create_car),
    path('api/car/5/', views.delete_car),
    path('api/cars/update/<int:pk>', views.update_car),
]
