from django.db import models
from django.contrib.auth.models import User


# Single task, written or with answers to choose
class Exercise(models.Model):
    name = models.CharField(max_length=50)  # Name of the exercise
    text = models.CharField(max_length=200)  # Content of the exercise
    written_exercise = models.BooleanField(default=False)  # True if student have to write answer
    max_points = models.DecimalField(max_digits=4, decimal_places=2)  # Maximum points that student can get


class PossibleAnswers(models.Model):
    key = models.CharField(max_length=10)
    value = models.CharField(max_length=100)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)


# Exam sheet
class Exam(models.Model):
    owner = models.ForeignKey(User, related_name='exams', on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    max_points = models.DecimalField(max_digits=5, decimal_places=2)


class AnswerSheet(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.DecimalField(max_digits=3, decimal_places=2)


class Answer(models.Model):
    answer_sheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    answer = models.ForeignKey(PossibleAnswers, on_delete=models.CASCADE, blank=True)
    written_answer = models.CharField(max_length=200, blank=True)
