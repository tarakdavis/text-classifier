from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import IndexView

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
