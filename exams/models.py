from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Single task, written or with answer to choose
class Exercise(models.Model):
    name = models.CharField(max_length=50)  # Name of the exercise
    text = models.CharField(max_length=200)  # Content of the exercise
    written_exercise = models.BooleanField(default=False)  # True if student have to write answer
    possible_answers = ArrayField(models.CharField(max_length=100),
                                  blank=True)  # If Exercise is not wriiten, araay of possible answer
    correct_answer = models.CharField(max_length=100)  # Correct answer
    max_points = models.DecimalField(max_digits=4, decimal_places=2)  # Maximum points taht student can get


# Exam sheet
class Exam(models.Model):
    owner = models.ForeignKey(User, related_name='exams', on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    points = models.DecimalField(max_digits=5, decimal_places=2)
    max_points = models.DecimalField(max_digits=5, decimal_places=2)


class Answers(models.Model):
    answer = models.CharField(max_length=100)  # Answer by student
    points = models.DecimalField(max_digits=4, decimal_places=2)  # Points received for the task
