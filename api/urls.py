from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('portfolio/', views.portfolio),
    path('team/', views.team),
    path('team-member/', views.team_member),
    path('service/', views.service),
    path('vacansy/', views.vacancy),
    path('vocancies_list', views.vacancies_list),
    path('vacansies-resume-create/', views.vacancies_resume_create),
    path('message-create/', views.message_create),
]