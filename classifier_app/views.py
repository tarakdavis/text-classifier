from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data
from .serializers import ClassifierSerializer, DataSerializer
from django.views.generic import TemplateView
# for the Pipeline
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.pipeline import Pipeline


def pipeline_predict(request):  # self, X_train, y_train, label, X_test, y_test
    self.X_train = X_train  # comes from DB
    self.y_train = y_train  # passed in ( calc'd first )
    self.label = label      # comes from user input
    self.X_test = X_test    # comes from user input
    self.y_test = y_test    # passed in ( calc'd first )

    py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
    py_pipeline.fit(X_train, y_train)
    prediction = py_pipeline.predict(X_test)
    score = py_pipeline.score(X_test, y_test)
    return prediction, score


# class IndexView(TemplateView):
#     template_name = 'classifier_app/index.html'
#
#
# class TrainView(TemplateView):
#     template_name = 'classifier_app/train.html'
#
#
# class PredictView(TemplateView):
#     template_name = 'classifier_app/predict.html'


class ClassifierViewSet(viewsets.ModelViewSet):
    serializer_class = ClassifierSerializer
    queryset = Classifier.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
