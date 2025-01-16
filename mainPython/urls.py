from django.urls import path
from . import views



urlpatterns = [
    path('', views.getMainPage, name = 'mainPage'),
    path('statistics/', views.general_statistics, name = 'generalStatistic'),
    path('demand/', views.demand, name = 'demand'),
    path('geography/', views.geography_statistics, name = 'geography'),
    path('skills/', views.skills_statistics, name = 'skills'),
    path('recent_jobs', views.recent_jobs, name = "recent_jobs"),
] 

