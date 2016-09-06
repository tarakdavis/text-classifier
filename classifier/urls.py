from django.conf.urls import url, include
from django.contrib import admin
from classifier_app import views
from rest_framework import routers

# from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'classifier', views.ClassifierViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = [
    url(r'^', include('classifier_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
