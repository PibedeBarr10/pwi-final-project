from django.urls import path
from django.conf.urls import url, include
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]