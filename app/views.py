from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView

from app.models import ToDo
from app.serializers import ToDoSerializer


#CRUD operation


class ListToDo(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UpdateToDo(UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDo(DestroyAPIView):   # delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer




