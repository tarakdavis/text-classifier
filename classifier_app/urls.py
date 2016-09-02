from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import IndexView, TrainView, PredictView

urlpatterns = [
    url(r'^train/$', views.TrainView.as_view(), name='train'),
    url(r'^predict/$', views.PredictView.as_view(), name='predict'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
