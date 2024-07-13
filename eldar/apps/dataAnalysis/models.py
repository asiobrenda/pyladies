from django.db import models

class Source(models.Model):
    class Meta:
        verbose_name_plural = ('Source')
        ordering = ['id']

    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Product(models.Model):
    class Meta:
        verbose_name_plural = ('Product')

    sitc2 = models.BigIntegerField(default=0, blank=True)
    description = models.CharField(max_length=200, default='', blank=True)


    def __str__(self):
        return str(self.sitc2) + str(self.description)

class YearData(models.Model):
    class Meta:
        verbose_name_plural = ('YearData')

    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='source_year_data', null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_year_data', null=False)
    year = models.SmallIntegerField(default=0, null=False, blank=False)
    values = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return str(self.source.id) + str(self.product.id) + str(self.year) + str(self.values)