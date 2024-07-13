from django.db import models

class City(models.Model):
    class Meta:
        verbose_name_plural = ('City')

    city_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    color = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.city_name

