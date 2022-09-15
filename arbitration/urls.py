from django.urls import path
from . import views

urlpatterns = [
    path('add_mark/', views.add_marks),
    # path('add_teams/', views.add_teams),
    path('audience_award/', views.audience_award),
    path('teams/', views.teams)
]
