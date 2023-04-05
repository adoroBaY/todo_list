from rest_framework import serializers

from todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = fields = "__all__"

class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id']
