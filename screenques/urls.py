from django.urls import path
from . import views

urlpatterns = [
    path("inter_action_ques/", views.inter_action_question),
    path("inter_action_question_move/", views.inter_action_question_move),
    path("inter_action_question_delete/", views.inter_action_question_delete)
]
