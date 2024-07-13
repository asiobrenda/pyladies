from django.db import models
from django.urls import reverse
class TennisClub(models.Model):

      class Meta:
          verbose_name_plural = ('TennisClub')

          ordering = ['id']


      # member_id = models.AutoField(primary_key=True)
      member_name = models.CharField(max_length=100)
      gender = models.CharField(max_length=100, blank=True)
      bio = models.TextField(max_length=500, blank=True, null=False)
      date_joined = models.DateField(auto_now=True)

      def get_absolute_url(self):
          return reverse('repeat:Update-member', kwargs={'pk':self.id})

      def __str__(self):
            return self.member_name


# class Person(models.Model):
#     user = models.OneToOneRel(on_delete=models.CASCADE)
#     profile = models.CharField(max_length=100)

class Author(models.Model):
    class Meta:
         verbose_name_plural = ('Author')
         ordering = ['id']

    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
         return self.name

class Books(models.Model):
    class Meta:
        verbose_name_plural = ('Books')

        ordering = ['id']

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE, related_name='authorbook')

    def __str__(self):
         return self.author

class CDistrict(models.Model):
    class Meta:
        verbose_name_plural = ('CDistrict')

    district_name = models.CharField(max_length=700, blank=True, null=False)

    def __str__(self):
        return self.district_name

class DistrictValue(models.Model):
    class Meta:
        verbose_name_plural = ('DistrictValue')

    district_name = models.ForeignKey(CDistrict, null=False, on_delete=models.CASCADE, related_name='county_data')
    year = models.SmallIntegerField(default=0, blank=False, null=False)
    district_value = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return str(self.district_name.id) + str(self.year) + str(self.district_value)
