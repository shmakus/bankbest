from django.urls import path, include

from . import views

app_name = 'search'
urlpatterns = [
    path(r'^$', views.ESearchView.as_view(), name='index')
]