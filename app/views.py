from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import ToDo
from app.serializers import ToDoSerializer


#CRUD operation


class ListToDo(APIView):
    def get(self, request):
        queryset = ToDo.objects.all()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)














# class UpdateToDo(UpdateAPIView):
   #  queryset = ToDo.objects.all()
    # serializer_class = ToDoSerializer

# class CreateTodo(CreateAPIView):
    # queryset = ToDo.objects.all()
    # serializer_class = ToDoSerializer

# class DeleteToDo(DestroyAPIView):   # delete
   #  queryset = ToDo.objects.all()
    # serializer_class = ToDoSerializer




