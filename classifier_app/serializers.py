from rest_framework import serializers
from .models import Classifier, Data
from django.contrib.auth.models import User


class ClassifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classifier
        fields = ('id', 'name')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'category', 'text', 'classifier')
