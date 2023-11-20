from django.urls import path
from . import views
urlpatterns = [
    path('', views.ThingsListView),
    path('show_detaill/<int:id>/', views.ThingsDeteilView)
]
