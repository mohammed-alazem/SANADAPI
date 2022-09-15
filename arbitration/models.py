from django.db import models


# Create your models here.
class JudgingMarks(models.Model):
    TeamNumber = models.IntegerField()
    JudgType = models.IntegerField()
    MarkAndQuestions = models.JSONField()


class Teams(models.Model):
    TeamNumber = models.IntegerField()
    Name = models.CharField(max_length=100)


class AudienceAward(models.Model):
    TeamNumber = models.IntegerField()
    Name = models.CharField(max_length=100)
    ID_Audience = models.CharField(max_length=100)


class ArbitrationType(models.Model):
    NumberType = models.IntegerField()
    Name = models.CharField(max_length=100)
