from django.core.management.base import BaseCommand 
from django.contrib.auth.models import Group, User,Permission
from django.contrib.contenttypes.models import ContentType
from polls.models import Question, PollSet, Choice
class Command(BaseCommand): 
    def handle(self, *args, **options): 
        new_group, created = Group.objects.get_or_create(name='Administrators')
         
        
        ctq = ContentType.objects.get_for_model(Question)  
        ctp = ContentType.objects.get_for_model(PollSet) 
        ctc = ContentType.objects.get_for_model(Choice) 
        # Now what - Say I want to add 'Can add project' permission to new_group?

        perms =[('Can add choice', ctc, 'add_choice'), 
                ('Can change choice', ctc, 'change_choice'), 
                ('Can delete choice', ctc, 'delete_choice'), 
                ('Can view choice', ctc, 'view_choice'), 
                ('Can add poll set', ctp, 'add_pollset'), 
                ('Can change poll set', ctp, 'change_pollset'), 
                ('Can delete poll set', ctp, 'delete_pollset'), 
                ('Can view poll set', ctp, 'view_pollset'), 
                ('Can add question', ctq, 'add_question'), 
                ('Can change question', ctq, 'change_question'), 
                ('Can delete question', ctq, 'delete_question'), 
                ('Can view question', ctq, 'view_question')
            ]

        for stat in perms:
            permission = Permission.objects.get(name=stat[0], codename=stat[2])
            print(stat[1])
            Group.objects.get(name='Administrators').permissions.add(permission) 