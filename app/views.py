from rest_framework import generics

from .models import ToDo
from .serializers import ToDoSerializer


#CRUD operation


class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# class DetailToDo(generics.RetrieveUpdateAPIView):
    # queryset = ToDo.objects.all()
    # serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# class DeleteToDo(generics.DestroyAPIView):   # delete
    # queryset = ToDo.objects.all()
    # serializer_class = ToDoSerializer




