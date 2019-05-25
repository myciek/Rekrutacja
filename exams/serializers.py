from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exams.models import Exercise


class UserSerializer(serializers.ModelSerializer):
    examples = serializers.PrimaryKeyRelatedField(many=True, queryset=Exercise.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'exercises')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ExerciseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exercise
        fields = ('text', 'owner')
