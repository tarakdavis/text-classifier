from django.shortcuts import render
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Classifier
from django.contrib.auth.views import login


# def index(request):
#     return HttpResponse('sup DAWG')
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
