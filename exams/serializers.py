from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exams.models import Exercise, Exam, PossibleAnswer, AnswerSheet, Answer


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('name', 'text', 'written_exercise', 'max_points')


class PossibleAnswerSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = PossibleAnswer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(PossibleAnswerSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that specified in the `fields` argument.
            not_allowed = set(fields)

            for field_name in not_allowed:
                self.fields.pop(field_name)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class ExamSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Exam
        fields = ('owner', 'subject', 'exercises', 'max_points')


class AnswerSheetSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    student = UserSerializer()

    class Meta:
        model = AnswerSheet
        fields = ('exam', 'student', 'points', 'grade')


class AnswerSerializer(serializers.ModelSerializer):
    answer_sheet = AnswerSheetSerializer()
    exercise = ExerciseSerializer()
    answer = PossibleAnswerSerializer(fields=('correct',))

    class Meta:
        model = Answer
        fields = ('answer_sheet', 'exercise', 'answer', 'written_answer')
