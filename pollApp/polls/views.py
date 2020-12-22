from django.shortcuts import render
from .serializers import QuestionSerializer, AnswerSerializer, PollSetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.views import  APIView
from rest_framework.response import Response
from .models import Question, PollSet
from rest_framework import viewsets,generics
from .models import Answer
from .serializers import UserAnswersSerializer


class QuestionsView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get(self, request):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)

class AllPollSetView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PollSetSerializer

    def get(self, request):
        sets = PollSet.objects.filter(active=True, )
        all_polls = PollSetSerializer(sets, many=True)
        return Response(all_polls.data)  

from django_filters.rest_framework import DjangoFilterBackend

class PollSetView(generics.ListAPIView):  
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['poll_set',] 
    
class QuestionAnswer(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})


class AllAnswers(generics.ListAPIView):
    serializer_class = UserAnswersSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Answer.objects.all()
        return queryset.filter(user=user)
