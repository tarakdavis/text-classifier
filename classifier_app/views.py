from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data
from .serializers import ClassifierSerializer, DataSerializer


# def index(request):
#     return HttpResponse('sup DAWG')
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    queryset = Classifier.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
