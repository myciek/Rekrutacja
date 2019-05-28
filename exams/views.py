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
class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsTeacher, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class PossibleAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = PossibleAnswerSerializer
    queryset = PossibleAnswer.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsTeacher, IsAuthenticated)


class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsTeacher, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnswerSheetViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSheetSerializer
    queryset = AnswerSheet.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticated,)
