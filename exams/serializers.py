# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exams.models import Exercise, Exam, PossibleAnswer, AnswerSheet, Answer, User


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class PossibleAnswerSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = PossibleAnswer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('subject', 'exercises', 'max_points')


class AnswerSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerSheet
        fields = ('exam', 'points', 'grade')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer_sheet', 'exercise', 'answer', 'written_answer')
