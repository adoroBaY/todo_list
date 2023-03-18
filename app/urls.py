from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListToDo.as_view(), name="todo_list"),
    path("create/", views.CreateTodo.as_view(), name="todo_create"),
    path("update/<int:pk>/", views.UpdateToDo.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteToDo.as_view(), name="delete")
]
