from django.shortcuts import get_object_or_404
from .models import Todo, Comment
from rest_framework.decorators import api_view
from .serializers import TodoSerializer, CommentSerializer
from rest_framework.response import Response


@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todo_create(request, todo_id):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(todo_id=todo_id)
        return Response(serializer.data)


@api_view(['GET'])
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_and_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'PUT':
        serializer = TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': ' todo_update'})
    else:
        todo.delete()
        return Response({'message': 'todo_delete'})


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, comment_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(todo_id=comment_id)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comment_update_and_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': ' comment_update'})
    else:
        comment.delete()
        return Response({'message': 'comment_delete'})
