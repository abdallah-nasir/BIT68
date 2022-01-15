from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as login_logic
from .serializers import Register_Serializer, Login_Serializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = Register_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = serializer.validated_data.get("username")
        token = Token.objects.get(user__username=user)
        message = {"message": f"user {user.title()} registered successfully", "token": token.key}
    else:
        message = serializer.errors
    return Response(message)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = Login_Serializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        token = Token.objects.get(user=user)
        login_logic(request, user)
        message = {"message": f"user {user.username.title()} logedin successfully", "token": token.key}
    else:
        message = serializer.errors
    return Response(message)
