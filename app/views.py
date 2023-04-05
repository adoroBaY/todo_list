from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import ToDo
from .serializers import ToDoSerializer, UsersSerializer


class ListToDo(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class UpdateToDo(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class CreateTodo(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DeleteToDo(DestroyAPIView):  # delete
    permission_classes = (IsAuthenticated,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {'token': token.key, 'user_id': serializer.instance.pk, 'username': serializer.instance.username},
            status=status.HTTP_201_CREATED)


class CustomAuthToken(ObtainAuthToken):
    permission_classes = (AllowAny,)
    throttle_classes = []
    authentication_classes = []
    serializer_class = AuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_created(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_created(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
