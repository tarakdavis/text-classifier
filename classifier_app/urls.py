from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import IndexView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'),
            name='register'),
]
