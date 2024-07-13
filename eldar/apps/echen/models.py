from django.db import models

class Client(models.Model):

      class Meta:
            verbose_name_plural = ('Client')
            ordering = ['id']

      name = models.CharField(max_length=100, blank=True, null=False)
      description = models.TextField(max_length=300, blank=True, null=False)
      image = models.ImageField(upload_to='client_images/', blank=True, null=False)

      def __str__(self):
            return self.name
