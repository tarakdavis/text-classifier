from django.conf.urls import url
from django.contrib import admin
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
# from .views import IndexView, TrainView, PredictView

app_name = 'classifier_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tt/$', views.pipeline_predict, name='tindex'),
    url(r'^train/$', views.train, name='train'),
    url(r'^predict/$', views.predict, name='predict'),
    url(r'^pipeline_predict/$', views.pipeline_predict, name='pipe'),
    # url(r'^train/$', views.TrainView.as_view(), name='train'),
    # url(r'^predict/$', views.PredictView.as_view(), name='predict'),
    # url(r'^predict/$', views.pipeline_predict, name='pipeline_predict')
    url(r'^accounts/profile/$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^register/$', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/'),
        name='register'),
]
