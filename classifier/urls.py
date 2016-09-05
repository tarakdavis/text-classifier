from django.conf.urls import url, include
from django.contrib import admin
from classifier_app import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'classifier', views.ClassifierViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = [
    url(r'^', include('classifier_app.urls')),
    url(r'^train2/$', views.pipeline_predict, name='training'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls))
    ]
