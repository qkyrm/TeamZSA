from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views
from .views import ThingsDetailView, ThingsListView
from .views import ThingsDetailView, ThingsListView, thing_update, thing_delete, page1, SweatListView, MugListView, \
    BagListView, TshirtListView, create_thing, things_list_view





urlpatterns = [
    # path('', ThingsListView, name='things_list'),
    path('show_detail/<int:id>/', ThingsDetailView, name='things_detail'),
    path('',ThingsListView, name='things'),
    path('page1/', page1, name="page1"),
    path('page2/', SweatListView, name="page2"),
    path('page3/', MugListView, name="page3"),
    path('page4/', BagListView, name="page4"),
    path('page5/', TshirtListView, name="page5"),
    path('things_list/', things_list_view, name='things_list'),
    path('create/', create_thing, name='create_thing'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('thing_update/<int:id>/', thing_update, name='thing_update'),
    path('things/<int:id>/delete/', thing_delete, name='thing_delete'),
]
