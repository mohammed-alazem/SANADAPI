from rest_framework import serializers
from arbitration.models import Teams,JudgingMarks


class TeamNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['Name']


class JudgeMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgingMarks
        fields = '__all__'
