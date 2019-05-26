from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exams.models import Exercise, Exam, PossibleAnswers, AnswerSheet, Answer


class PossibleAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAnswers
        fields = ('key', 'value')


class ExerciseSerializer(serializers.ModelSerializer):
    possible_answers = PossibleAnswersSerializer(many=True)

    class Meta:
        model = Exercise
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(ExerciseSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop fields specified in the 'fields' argument.
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
        fields = ('owner', 'exercises', 'max_points')


class AnswerSheetSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    student = UserSerializer()

    class Meta:
        model = AnswerSheet
        fields = ('exam', 'student', 'points', 'grade')


class AnswerSerializer(serializers.ModelSerializer):
    answer_sheet = AnswerSheetSerializer()
    exercise = ExerciseSerializer(fields=('correct_answer',))
    answer = PossibleAnswersSerializer()

    class Meta:
        model = Answer
        fields = ('answer_sheet', 'exercise', 'answer', 'written_answer')
