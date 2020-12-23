from django.contrib import admin

from django.contrib import admin
from .models import Question, Answer, Choice, PollSet

from .models import AnonymousAnswer, AnonymousUser


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
        'pk',
    )
 
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'points',
        'lock_other',
        'pk',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
        'pk',
    )
    list_filter = ('user',)

class PollSetAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'start_date',
        'expiration_date',
        'pk',
    ) 

class AnonymousUserAdmin(admin.ModelAdmin):
    ''' модель приложения users '''
    list_display = (
        'user', 
        'created', 
    )
    list_filter = ('user',)

class AnonymousAnswerAdmin(admin.ModelAdmin):
    ''' модель приложения users '''
    list_display = (
        'user',
        'question',
        'choice',
        'pk',
    )
    list_filter = ('user',)


admin.site.register(AnonymousUser, AnonymousUserAdmin)
admin.site.register(AnonymousAnswer, AnonymousAnswerAdmin)
admin.site.register(PollSet, PollSetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)

