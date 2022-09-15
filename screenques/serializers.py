from rest_framework import serializers
from .models import TempList, InterActionQuestion


class TempListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TempList
        fields = '__all__'


class InterActionQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = InterActionQuestion
        fields = '__all__'
