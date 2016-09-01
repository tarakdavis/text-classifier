from django.db import models
from django.contrib.auth.models import User


class Classifier(models.Model):
    name = models.CharField(max_length=100, is_visible=False)

    def train():
        pass

    def predict():
        pass


class Data(models.Model):
    category = models.CharField(max_length=100)
    text = models.TextField()
    classifier = models.ForeignKey(Classifier)
