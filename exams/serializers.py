from django.contrib.auth.models import User, Group
from rest_framework import serializers
from exams.models import Example


class UserSerializer(serializers.ModelSerializer):
    examples = serializers.PrimaryKeyRelatedField(many=True, queryset=Example.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'examples')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ExampleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Example
        fields = ('text','owner')
