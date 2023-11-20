from django.urls import path
# from . import views
from .views import ThingsDeteilView, ThingsListView
urlpatterns = [
    path('', ThingsListView),
    path('show_detaill/<int:id>/', ThingsDeteilView)
]
