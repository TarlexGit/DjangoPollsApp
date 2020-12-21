from django.contrib import admin

from django.contrib import admin
from .models import Question, Answer, Choice, PollSet


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
    )
 
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'points',
        'lock_other',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)

class PollSetAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'start_date',
        'expiration_date',
    ) 

admin.site.register(PollSet, PollSetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
