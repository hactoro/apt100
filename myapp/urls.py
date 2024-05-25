from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('helloworld', views.helloworld, name='helloworld'),
    path('getApt100', views.getApt100, name='getApt100' )

]