from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# from polls.models import Question


# class UserFilesViewSet(viewsets.ViewSet): 
#     permission_classes = (IsAuthenticated, )
#     def list(self, request):
#         queryset = UpFiles.objects.filter(client_id=request.user)
#         serializer = UpFilesSerializer(queryset, many=True)
#         return Response(serializer.data)
 
# class GetUserToken(APIView):
#     def get(self, request, format=None):
#         queryset = UserVerificationToken.objects.filter(user=request.user)
#         serializer = TokenSerializer(queryset, many=True)
#         return Response(serializer.data)
