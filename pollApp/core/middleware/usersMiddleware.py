from polls.models import AnonymousUser

#########3  неудачная попытка, SimpleMiddleware не подключен в settings.
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request): 
        if not request.user.is_authenticated:
            user_id = AnonymousUser.objects.create(data=request.META)
            response = self.get_response(request) 
            response.set_cookie('AnonymousUser', value=user_id.pk, secure=None, httponly=True)  
        else:  
            response = self.get_response(request)  
        return response 