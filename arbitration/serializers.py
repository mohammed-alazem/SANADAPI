from rest_framework import serializers
from .models import JudgingMarks, Teams, AudienceAward


class JudgingMarksSerializers(serializers.ModelSerializer):
    class Meta:
        model = JudgingMarks
        fields = '__all__'


class TeamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class AudienceAwardSerializers(serializers.ModelSerializer):
    class Meta:
        model = AudienceAward
        fields = '__all__'
