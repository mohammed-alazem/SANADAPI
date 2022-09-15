from django.urls import path
from . import views

urlpatterns = [
    path("vote_excel/", views.vote_excel),
    path("judge_excel/",views.judge_excel)
]
