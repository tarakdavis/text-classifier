from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data
from .serializers import ClassifierSerializer, DataSerializer
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse('sup DAWG')
# Create your views here.
class IndexView(TemplateView):
    template_name = 'classifier_app/index.html'


class TrainView(TemplateView):
    template_name = 'classifier_app/train.html'


class PredictView(TemplateView):
    template_name = 'classifier_app/predict.html'


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    queryset = Classifier.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
