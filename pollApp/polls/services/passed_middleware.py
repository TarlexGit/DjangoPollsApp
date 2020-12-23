from polls.models import AnonymousUser
from django.http import HttpResponse
from rest_framework.response import Response

def freshen_up_AnonymousUser(request): 
    user_id = AnonymousUser.objects.create(data=request.META) 
    response = Response({'result': 'OK'}) 
    response.set_cookie('AnonymousUser', value=user_id.pk, secure=None, httponly=True)
    return response