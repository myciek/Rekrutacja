from django.db import models


# Create your models here.


class Example(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='examples', on_delete=models.CASCADE)
