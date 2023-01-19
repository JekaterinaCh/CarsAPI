from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    class Meta:
        app_label = 'registration'
