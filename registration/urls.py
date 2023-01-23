from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/cars/<int:pk>', views.cars_detail),
    path('api/cars/', views.cars_list),
]
