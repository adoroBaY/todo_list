from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/', DetailToDo.as_view(), name="details"),
    path('', ListTodo.as_view(), name="list"),
    #path('update/<int:pk>/', UpdateToDo.as_view(), name="update"),
    path('create', CreateTodo.as_view(), name="create"),
    path('delete/<int:pk>', DeleteToDo.as_view(), name="delete")
]