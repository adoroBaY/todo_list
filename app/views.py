from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework import generics

from .models import *
from .serializers import *


#CRUD operation
class ListTodo(generics.ListAPIView):     #read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):  #udate
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):    # create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDo(generics.DestroyAPIView):   # delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer




