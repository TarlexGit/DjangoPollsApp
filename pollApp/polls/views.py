from django.shortcuts import render
from .serializers import QuestionSerializer, AnswerSerializer, PollSetSerializer, AnonymousAnswerSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import  APIView
from rest_framework.response import Response
from .models import Question, PollSet, Answer, AnonymousUser, AnonymousAnswer
from rest_framework import generics
from .serializers import UserAnswersSerializer, AnonUserAnswersSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from .services.passed_middleware import freshen_up_AnonymousUser
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404  


class QuestionsView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get(self, request):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)

class AllPollSetView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = PollSetSerializer

    def get(self, request):
        sets = PollSet.objects.filter(active=True, )
        all_polls = PollSetSerializer(sets, many=True)
        return Response(all_polls.data)  

class PollSetView(generics.ListAPIView):  
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['poll_set',] 
    
class QuestionAnswer(generics.GenericAPIView):
    serializer_class = AnswerSerializer 
 
    def post(self, request, format=None): 
        if request.user.is_authenticated:
            answer = AnswerSerializer(data=request.data, context=request) 
            if answer.is_valid(raise_exception=True):
                answer.save()
                return Response({'result': 'OK'})
                 
        else: 
            try: 
                get_object_or_404(AnonymousUser, pk=request.COOKIES['AnonymousUser'])
                answer = AnonymousAnswerSerializer(data=request.data, context=request) 
                if answer.is_valid(raise_exception=True):
                    answer.save() 
                    return Response({'result': 'OK'}) 
            except:
                user_id = AnonymousUser.objects.create(data=request.META)
                request.COOKIES['AnonymousUser']=user_id.pk
                response = Response({'result': 'OK'}) 
                response.set_cookie('AnonymousUser', value=user_id.pk, secure=None, httponly=True) 

            answer = AnonymousAnswerSerializer(data=request.data, context=request) 
            if answer.is_valid(raise_exception=True):
                answer.save() 
                return response

 

class AllAnswers(APIView): 
    def get(self, request):
        # print('---------', request.COOKIES['AnonymousUser'])
        if request.user: 
            print('request.user', request.user)
            try:
                queryset = Answer.objects.filter(user=request.user)
                all_answers = UserAnswersSerializer(queryset, many=True )
                return Response(all_answers.data)
            except:
                print(request.COOKIES['AnonymousUser'])
        # elif request.user == "AnonymousUser" and 'AnonymousUser' in request.COOKIES:  
        #     queryset = AnonymousAnswer.objects.filter(pk=request.COOKIES['AnonymousUser'])
        #     all_answers = AnonUserAnswersSerializer(queryset, many=True )
        #     return Response(all_answers.data )
        # else: 
                queryset = AnonymousAnswer.objects.filter(user=request.COOKIES['AnonymousUser'])
                all_answers = AnonUserAnswersSerializer(queryset, many=True)
                return Response(all_answers.data )