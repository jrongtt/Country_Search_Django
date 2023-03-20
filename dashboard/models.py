from django.db import models

# Create your models here.
class Data(models.Model):
    country_name = models.CharField(max_length=100)
    flag = models.CharField(max_length=2, default='')
    size = models.PositiveBigIntegerField(default=0)
    population = models.PositiveBigIntegerField(default=0)
    capital_city = models.CharField(max_length=100, default='')
    # description = models.TextField()

    def __str__(self):
        return self.country_name