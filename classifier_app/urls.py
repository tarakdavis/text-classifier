from django.conf.urls import url
from django.contrib import admin
from . import views
# from .views import IndexView, TrainView
# PredictView

app_name = 'classifier_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tt/$', views.pipeline_predict, name='tindex'),
    url(r'^train/$', views.train, name='train'),
    url(r'^predict/$', views.predict, name='predict'),
    url(r'^pipeline_predict/$', views.pipeline_predict, name='pipe'),
    # url(r'^new_train/$', views.new_train, name='new_train'),

    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'$', views.pipeline_predict),
    # url(r'^predict/$', views.predict, name='predict'),  # T
    # url(r'^train/$', views.TrainView.as_view(), name='train'),
    # url(r'^predict/$', views.PredictView.as_view(), name='predict'),
    # url(r'^predict/$', views.pipeline_predict, name='pipeline_predict')
]
