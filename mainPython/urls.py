from django.urls import path
from . import views



urlpatterns = [
    path('', views.getMainPage, name = 'mainPage'),
    path('statistics/', views.general_statistics, name = 'generalStatistic'),
] 

