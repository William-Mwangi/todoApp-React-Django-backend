from django.shortcuts import get_object_or_404, render
from .models import todo
from .serializers import todoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["GET", "POST"])
def todo_list(request):
    if request.method == "GET":
        todoList = todo.objects.all()
        serializer = todoSerializer(todoList, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = todoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail(request, pk):
    Todo = get_object_or_404(todo, id=pk)

    if request.method == "PATCH":
        serializer = todoSerializer(Todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        Todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "GET":
        serializer = todoSerializer(Todo)
        return Response(serializer.data)
