from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data, Document
from .serializers import ClassifierSerializer, DataSerializer
from django.views.generic import TemplateView
from django.views import generic
from rest_framework.decorators import api_view
import re
# from csv_reader import get_text_data
# for the Pipeline
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.pipeline import Pipeline
from collections import defaultdict

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .forms import DocumentForm

def index(request):
    return render(request, 'classifier_app/index.html')


def train(request):
    return render(request, 'classifier_app/train.html')


def predict(request):
    return render(request, 'classifier_app/predict.html')


def delete(request):
    return render(request, 'classifier_app/delete.html')


def classifier_delete(request):
    # delete an object and send a confirmation response
    x = str(request)
    y = int(re.findall(r'[0-9]+', x)[0])
    dele = Classifier.objects.get(pk=y)
    dele.delete()
    return render(request, 'classifier_app/delete.html')
    # Classifier.objects.get(pk=request.DELETE['pk']).delete()
    # return HttpResponse()


def data_delete(request):
    # delete an object and send a confirmation response
    x = str(request)
    y = int(re.findall(r'[0-9]+', x)[0])
    dele = Data.objects.get(pk=y)
    dele.delete()
    return render(request, 'classifier_app/delete.html')


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = Document(docfile=request.FILES['docfile'])
            new_doc.save()
            return HttpResponseRedirect(reverse('classifier_app.views.upload_file'))
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render_to_response('classifier_app/upload_file.html',
                            {'documents': documents, 'form': form})


def import_csv(request):#, csv_file_name):
    # imported_text = get_text_data(csv_file_name)
    #parse it - clean it
    #add to DB
    return render ( request, 'classifier_app/successful_import.html')

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
    py_pipeline = Pipeline([("count", CV()),
                            # ("tfid", TF()),
                            ("multi", MNB())])
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


# class IndexView(TemplateView):
#     template_name = 'classifier_app/index.html'
#
#
# class TrainView(TemplateView):
#     template_name = 'classifier_app/train.html'
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
