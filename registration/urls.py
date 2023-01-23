from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/cars/get/<int:pk>', views.cars_view, name='cars_view'),
    # path('api/cars/get/', views.cars_view, {'pk': None}, name='cars_view'),
    # path('api/cars/create/', views.create_car),
    # path('api/cars/delete/<int:pk>', views.delete_car),
    path('api/cars/<int:pk>', views.cars_detail),
    path('api/cars/', views.cars_list),
]
