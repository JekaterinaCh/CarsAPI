from rest_framework import serializers
from .models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('name', 'year')
        db_table = 'Cars'
