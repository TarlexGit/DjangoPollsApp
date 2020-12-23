from django.db import models 
from django.contrib.auth.models import User


class PollSet(models.Model):
    title = models.CharField(max_length=100) 
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()
    poll_set = models.ForeignKey(PollSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Answer(models.Model): 
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True) 
    poll_set = models.ForeignKey(PollSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice.title 


class AnonymousUser(models.Model):
    ''' возможно обернуть в AbstractUser для предсоздания юзера и последущей регистрации '''
    user = models.AutoField(primary_key=True)
    data = models.CharField(max_length=1000, blank=True, null=True) # для метадаты, айпишника и других первичныхх отпечатков
    created = models.DateTimeField(auto_now_add=True) 

class AnonymousAnswer(models.Model):  
    ''' модель только для анонимных пользователей  ''' 
    user = models.ForeignKey(AnonymousUser, verbose_name='user', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True) 
    poll_set = models.ForeignKey(PollSet, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.choice.title

    class Meta:
        get_latest_by = 'created'