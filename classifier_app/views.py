from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data
from .serializers import ClassifierSerializer, DataSerializer
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse

from rest_framework.decorators import api_view

# for the Pipeline
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.pipeline import Pipeline
from collections import defaultdict



def index(request):
    return render(request, 'classifier_app/index.html')


def train(request):
    return render(request, 'classifier_app/train.html')


def predict(request):
    return render(request, 'classifier_app/predict.html')


# def new_classif(request):
#     if request.method == 'POST':
#         preclas = request.POST.get('newClass')
#
#
# def new_train(request):
#     if request.method == 'POST':
#         preclas = request.POST.get('newClass')
#         precat = request.POST.get('newCat')
#         pretext = request.POST.get('newText')
#         print("===========================", preclas, precat, pretext)
#
#     context = {'response': "preclas" + "precat" + "pretext"}
#     return render(request, 'classifier_app/tindex.html', context)


def pipeline_predict(request):
    if request.method == 'POST':
        preTest = request.POST.get('text_to_classif')
        predictTestData = preTest.split()
        print("*********************", predictTestData)
    py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
    dbData = Data.objects.all()
    X_language_train = []
    y_language_train = []
    for each in dbData:
        xlt = each.text.split(", ")
        ylt = len(each.text.split(", "))*[each.category]
        X_language_train.extend(xlt)
        y_language_train.extend(ylt)
    print(X_language_train, y_language_train)
    py_pipeline.fit(X_language_train, y_language_train)
    prediction = py_pipeline.predict(predictTestData)
    print("*********************", prediction)
    appearances = defaultdict(int)
    for curr in prediction:
        appearances[curr] += 1
    answer = max(appearances, key=appearances.get)
    print("*********************", answer)
    # score = py_pipeline.score(span_test_data, y)
    context = {
        'response': answer
    }
    return render(request, 'classifier_app/tindex.html', context)

# from ART =======================================================================================

# def anotherFUNC(request, pk):  # self, X_train, y_train, label, X_test, y_test
#     if request.method == 'POST':
#         print("Posted")
#         form = TrainDataForm(request.POST)
#         if form.is_valid():
#             var = request.POST['user_input']
#             print('user input', var)
#     else:
#         print("didn't post")
# 	context = {
#         'var': var,
#     }
# 	return render(request, 'classifier_app/train.html', context)

# from ART =======================================================================================

# class IndexView(TemplateView):
#     template_name = 'classifier_app/index.html'
#
#
# class TrainView(TemplateView):
#     template_name = 'classifier_app/train.html'
#
#
# class PredictView(generic.ListView):
#     template_name = 'classifier_app/predict.html'
#     context_object_name = 'data_list'
#
#     def get_queryset(self):
#         return Data.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(PredictView, self).get_context_data(**kwargs)
#         context['classifier_list'] = Classifier.objects.all()
#         return context


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    queryset = Classifier.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
