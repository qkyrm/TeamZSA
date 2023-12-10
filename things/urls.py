from django.urls import path
from . import views
from .views import ThingsDetailView, ThingsListView
urlpatterns = [
    path('', ThingsListView),
    path('show_detail/<int:id>/', ThingsDetailView , name='things_detail'),
    path('page1', views.page1, name="page1"),
    path('page2', views.SweatListView, name="page2"),
    path('page3', views.MugListView, name="page3"),
    path('page4', views.BagListView, name="page4"),
    path("page5", views.TshirtListView, name="page5"),
]
