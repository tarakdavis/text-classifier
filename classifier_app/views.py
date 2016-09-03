from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data
from .serializers import ClassifierSerializer, DataSerializer
from django.views.generic import TemplateView
from django.views import generic
# for the Pipeline
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.pipeline import Pipeline


def pipeline_predict(request, pk):  # self, X_train, y_train, label, X_test, y_test
    # self.X_train = X_train  # comes from DB
    # self.y_train = y_train  # passed in ( calc'd first )
    # self.label = label      # comes from user input
    # self.X_test = X_test    # comes from user input
    # self.y_test = y_test    # passed in ( calc'd first )
    classifier = Classifier.object.get(id=2)
    py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
    data_set = classifier.data_set.all()
    py_pipeline.fit()
    prediction = py_pipeline.predict('hola')
    score = py_pipeline.score(X_test, y_test)
    return prediction, score
# def index(request):
#     return HttpResponse('hello world')


def train(request, classifier_id):  # self, X_train, y_train, label, X_test, y_test
    all_objects = Classifier.objects.get(id=classifier_id)
    # all_objects = Data.objects.all()

    X_train = all_objects.text  # comes from DB
    label = all_objects.category    # comes from user input

    y_train = label * X_train  # passed in ( calc'd first )
    # X_test =    # comes from user input
    # y_test =   # passed in ( calc'd first )

    py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
    py_pipeline.fit(X_train, y_train)
    # prediction = py_pipeline.predict(X_test)
    # score = py_pipeline.score(X_test, y_test)
    # return prediction, score
    return py_pipeline


def predict(request, py_pipeline, X_test):
    prediction = py_pipeline.predict(X_test)
    # score = py_pipeline.score(X_test, y_test)
    return prediction


class IndexView(TemplateView):
    template_name = 'classifier_app/index.html'


class TrainView(TemplateView):
    template_name = 'classifier_app/train.html'


class PredictView(generic.ListView):
    template_name = 'classifier_app/predict.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return Data.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PredictView, self).get_context_data(**kwargs)
        context['classifier_list'] = Classifier.objects.all()
        return context


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    queryset = Classifier.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
