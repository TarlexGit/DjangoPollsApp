from django.urls import path

from . import views

urlpatterns = [
    path("questions/", views.QuestionsView.as_view(), name="one"),
    path("answer/", views.QuestionAnswer.as_view(), name="two"),
    path("pollsets/", views.AllPollSetView.as_view(), name="GetPollSet"),
    path("poll/", views.PollSetView.as_view(), name="PollSetView"),
]