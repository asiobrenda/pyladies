from django.db import models


class County(models.Model):
    class Meta:
        verbose_name_plural = ('County')

    country = models.CharField(max_length=700, blank=True, null=False)

    def __str__(self):
        return self.country

class CountyValue(models.Model):
    class Meta:
        verbose_name_plural = ('CountyValue')

    county = models.ForeignKey(County, null=False, on_delete=models.CASCADE, related_name='county_data')
    years = models.SmallIntegerField(default=0, blank=False, null=False)
    value_data = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return str(self.county.id) + str(self.years) + str(self.value_data)
