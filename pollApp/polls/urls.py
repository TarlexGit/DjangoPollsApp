from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path("questions/", views.QuestionsView.as_view(), name="one"),
    path("answer/", views.QuestionAnswer.as_view(), name="two"),
    path("pollsets/", views.AllPollSetView.as_view(), name="GetPollSet"),
    path("poll/", views.PollSetView.as_view(), name="PollSetView"),
    path("user/answer/", views.AllAnswers.as_view(), name="AllAnswers"),
 
]