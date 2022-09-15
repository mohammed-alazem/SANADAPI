from django.db import models


# Create your models here.
class TempList(models.Model):
    Name = models.CharField(max_length=100)
    Answer = models.CharField(max_length=1000)


class InterActionQuestion(models.Model):
    Name = models.CharField(max_length=100)
    Answer = models.CharField(max_length=1000)
