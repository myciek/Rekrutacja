from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from exams.models import Example
from exams.serializers import ExampleSerializer
from rest_framework import status, permissions
from exams.permissions import IsOwnerOrReadOnly


# Create your views here.

class ExampleList(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        race = Example.objects.all()
        serializer = ExampleSerializer(race, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)