from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(verbose_name=None)

    def __str__(self):
        return self.name
