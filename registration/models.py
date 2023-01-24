from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(max_length=255)

    class Meta:
        db_table = 'Cars'
        app_label = 'registration'
