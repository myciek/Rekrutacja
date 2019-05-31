from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_teacher', False)
        return self._create_user(username, email, password, **extra_fields)


# Single task, written or with answers to choose
class Exercise(models.Model):
    owner = models.ForeignKey(User, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # Name of the exercise
    text = models.CharField(max_length=200)  # Content of the exercise
    written_exercise = models.BooleanField(default=False)  # True if student have to write answer
    max_points = models.DecimalField(max_digits=4, decimal_places=2)  # Maximum points that student can get

    def __str__(self):
        return self.name


class PossibleAnswer(models.Model):
    key = models.CharField(max_length=10)
    value = models.CharField(max_length=100)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.key


# Exam sheet
class Exam(models.Model):
    owner = models.ForeignKey(User, related_name='exams', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, blank= True)
    max_points = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.subject + " Exam"


class AnswerSheet(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    grade = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default=2)

    def __str__(self):
        return "Answers to " + str(self.exam)


class Answer(models.Model):
    answer_sheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    answer = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE, blank=True, null=True)
    written_answer = models.CharField(max_length=200, blank=True)
    points = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return "Answer to " + str(self.exercise)
