from django.urls import path

from . import views, goauth2

urlpatterns = [
    path('', views.index, name='index'),
    path('goauth2token', goauth2.verify, name='verify')
]
