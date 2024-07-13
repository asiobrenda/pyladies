from django.db import models
from django.contrib.postgres.fields import JSONField

class City(models.Model):
    class Meta:
        verbose_name_plural = ('City')

    city_name = models.CharField(max_length=500)
    color = models.CharField(max_length=300)
    description = models.CharField(max_length=600)
    save_btn = JSONField(null=True)

    def __str__(self):
        return self.color + self.description


class Client(models.Model):
    class Meta:
        verbose_name_plural = ('Client')

    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=300)

    def __str__(self):
        return self.name + self.gender