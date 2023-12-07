
from django.urls import path

from . import views
from .views import ThingsDeteilView, ThingsListView
urlpatterns = [
    path('', ThingsListView),
    path('show_detaill/<int:id>/', ThingsDeteilView),
    path('home', views.home, name="home"),
    path('page1', views.page1, name="page1"),
    path('page2', views.SweatListView, name="page2"),
    path('page3', views.MugListView, name="page3"),
    path('page4', views.BagListView, name="page4"),
    path("page5", views.TshirtListView, name="page5"),
]
