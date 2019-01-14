from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='mainWindow' ),
    url(r'^$', views.search),
]

