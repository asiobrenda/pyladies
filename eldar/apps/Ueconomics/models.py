from django.db import models

class Source(models.Model):
    class Meta:
        verbose_name_plural = ('Source')
        ordering = ['id']

    type = models.CharField(max_length=100, blank=True, null=False)

    def __str__(self):
        return self.type

class Product(models.Model):
    class Meta:
        verbose_name_plural = ('Product')
        ordering = ['id']


    sitc2 = models.PositiveIntegerField(null=False, blank=True)
    description = models.CharField(max_length=200, blank=True, null=False)

    def __str__(self):
        return str(self.sitc2) + str(self.description)

class YearData(models.Model):
    class Meta:
        verbose_name_plural = ('YearData')
        ordering = ['id']


    source = models.ForeignKey(Source, null=False, on_delete=models.CASCADE, related_name='source_type')
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name='product')
    year = models.BigIntegerField(default=0, null=False, blank=True)
    value = models.BigIntegerField(default=0, null=False, blank=True)

    def __str__(self):
        return str(self.source.id) + str(self.product.id) + str(self.year) + str(self.value)


class Cities(models.Model):
    class Meta:
        verbose_name_plural = ('Cities')

    name = models.CharField(max_length=500)
    color = models.CharField(max_length=300)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name + self.color + self.description
