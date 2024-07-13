from django.db import models


class Tabs(models.Model):
    class Meta:
        verbose_name_plural = ('Tabs')

    name = models.CharField(max_length=500)
    color = models.CharField(max_length=300)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name + self.color + self.description
