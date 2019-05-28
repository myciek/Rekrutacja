from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from exams.models import Exercise, PossibleAnswer, Exam, AnswerSheet, Answer, User
from exams.serializers import PossibleAnswerSerializer, ExerciseSerializer, ExamSerializer, AnswerSheetSerializer, \
    AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from exams.permissions import IsTeacher, IsOwnerOrReadOnly
from rest_framework import generics, viewsets
from django.http import Http404


# Create your views here.

class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsTeacher, IsOwnerOrReadOnly, IsAuthenticated)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, Exercise)
        serializer.save()


class PossibleAnswerList(generics.ListCreateAPIView):
    queryset = PossibleAnswer.objects.all()
    serializer_class = PossibleAnswerSerializer
    permission_classes = (IsTeacher, IsOwnerOrReadOnly, IsAuthenticated)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, PossibleAnswer)
        serializer.save()


class ExamList(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (IsTeacher, IsOwnerOrReadOnly, IsAuthenticated)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, Exam)
        serializer.save()


class AnswerSheetList(generics.ListCreateAPIView):
    queryset = AnswerSheet.objects.all()
    serializer_class = AnswerSheetSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, AnswerSheet)
        serializer.save()


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, Answer)
        serializer.save()
