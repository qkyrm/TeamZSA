
from django.urls import path

from . import views
from .views import ThingsDeteilView, ThingsListView
urlpatterns = [
    path('', ThingsListView),
    path('show_detaill/<int:id>/', ThingsDeteilView),
    path('', views.page1, name="page1"),
    path('page2', views.page2, name="page2"),
    path('page3', views.page3, name="page3"),
    path('page3', views.page4, name="page4"),
]
