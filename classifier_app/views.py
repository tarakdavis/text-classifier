from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from rest_framework import viewsets
from .models import Classifier, Data
from .serializers import ClassifierSerializer, DataSerializer
from django.views.generic import TemplateView
from django.views import generic
from . import forms
# for the Pipeline
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.pipeline import Pipeline


def pipeline_predict(request):  # self, X_train, y_train, label, X_test, y_test
    form = forms.TrainDataForm()
    if request.method == 'POST':
        form = forms.TrainDataForm(request.POST)
        if form.is_valid():
            print("good job!")
            # var = request.POST.get('user_input')
            user_text = form.cleaned_data['my_text']
            form.save()
            print('user_text: ', user_text)
            x_train = user_text.split()
            print('x_train: ', x_train)
            label = form.cleaned_data['my_category']
            print('label: ', label)
            y_train = [label] * len(x_train)
            print('y: ', y_train)
            py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
            py_pipeline.fit(x_train, y_train)
            prediction = py_pipeline.predict('hello my friend')
            print('prediction: ', prediction[0])
            # print('var', var, type(var))
            # print('user input', var)
    # else:
    #     print("didn't post")
        context = {'prediction': prediction}
        return HttpResponseRedirect(reverse('training'), context)
        # return render(request, 'classifier_app/train2.html', context)
    # self.X_train = X_train  # comes from DB
    # self.y_train = y_train  # passed in ( calc'd first )
    # self.label = label      # comes from user input
    # self.X_test = X_test    # comes from user input
    # self.y_test = y_test    # passed in ( calc'd first )
    # classifier = Classifier.object.get(id=2)
    # py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
    # data_set = classifier.data_set.all()
    # py_pipeline.fit()
    # prediction = py_pipeline.predict('hola')
    # context = {
    #     'var': var,
    # }
    # score = py_pipeline.score(X_test, y_test)
    # return HttpResponseRedirect(reverse('classifier_app:train'), var)
    # return render(request, 'classifier_app/train.html', context)
    return render(request, 'classifier_app/train2.html', {'form': form})
    # return prediction, score


def index(request):
    return render(request, 'classifier_app/index.html')
    # return HttpResponse('hello world')


def train(request):
    return render(request, 'classifier_app/train.html')


def predict(request):
    return render(request, 'classifier_app/predict.html')


# def train(request, classifier_id):  # self, X_train, y_train, label, X_test, y_test
#     all_objects = Classifier.objects.get(id=classifier_id)
#     # all_objects = Data.objects.all()
#
#     X_train = all_objects.text  # comes from DB
#     label = all_objects.category    # comes from user input
#
#     y_train = label * X_train  # passed in ( calc'd first )
#     # X_test =    # comes from user input
#     # y_test =   # passed in ( calc'd first )
#
#     py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])
#     py_pipeline.fit(X_train, y_train)
#     # prediction = py_pipeline.predict(X_test)
#     # score = py_pipeline.score(X_test, y_test)
#     # return prediction, score
#     return py_pipeline
#
#
# def predict(request, py_pipeline, X_test):
#     prediction = py_pipeline.predict(X_test)
#     # score = py_pipeline.score(X_test, y_test)
#     return prediction


# class IndexView(TemplateView):
#     template_name = 'classifier_app/index.html'


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
