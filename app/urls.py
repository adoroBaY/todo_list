from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk>/', DetailToDo.as_view(), name="details"),
    path('list', views.ListTodo.as_view(), name="list"),
    # path('update/<int:pk>/', UpdateToDo.as_view(), name="update"),
    path('', views.CreateTodo.as_view()),
    # path('delete/<int:pk>', DeleteToDo.as_view(), name="delete")
]
