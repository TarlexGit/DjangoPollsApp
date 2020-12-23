from rest_framework import serializers
from .models import Answer, Question, Choice, PollSet, AnonymousUser, AnonymousAnswer
from rest_framework.generics import get_object_or_404


class ChoiceSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()
    class Meta:
        model = Choice
        fields = ['pk', 'title', 'points', 'percent', 'lock_other', ]

    def get_percent(self, obj):
        total = Answer.objects.filter(question=obj.question).count()
        current = Answer.objects.filter(question=obj.question, choice=obj).count()
        if total != 0:
            return float(current * 100 / total)
        else:
            return float(0)

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )

    class Meta:
        model = Question
        fields = ['pk', 'title', 'choices', 'max_points', 'poll_set', ]

class PollSetSerializer(serializers.ModelSerializer):   
    class Meta:
        model = PollSet
        fields = ['pk', 'title',]
        
class UserAnswersSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Answer
        fields = '__all__'

class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()
    poll_set=serializers.JSONField()
    def validate_answers(self, answers):
        if not answers:
            raise serializers.Validationerror("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        poll_set=self.data['poll_set']
        user = self.context.user

        for answer in answers: 
            question = Question.objects.get(pk=answer[0])
            choices = answers[answer]

            for choice_id in choices: 
                Answer(user=user, question=question, choice=Choice.objects.get(pk=choice_id), poll_set=PollSet.objects.get(pk=poll_set)).save()
                user.is_answer = True
                user.save()

#### AnonymousAnswer
class AnonymousAnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()
    poll_set=serializers.JSONField()
    def validate_answers(self, answers):
        if not answers:
            raise serializers.Validationerror("Answers must be not null.")
        return answers

    def save(self): 
        answers = self.data['answers']
        poll_set=self.data['poll_set']
        user = AnonymousUser.objects.get(pk=self.context.COOKIES['AnonymousUser'])
        
        for answer in answers: 
            question = Question.objects.get(pk=answer[0])
            choices = answers[answer]

            for choice_id in choices: 
                try:
                    get_object_or_404(AnonymousAnswer,user=user, question=question)
                    print(' in models')
                    return {'error': 'answer is ready'}
                    # pass
                except:
                    AnonymousAnswer(user=user, question=question, choice=Choice.objects.get(pk=choice_id), poll_set=PollSet.objects.get(pk=poll_set)).save()
                    