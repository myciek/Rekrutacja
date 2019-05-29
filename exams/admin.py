from django.contrib import admin
from exams.models import Exercise, Exam, PossibleAnswer, AnswerSheet, Answer, User

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Exam)
admin.site.register(PossibleAnswer)
admin.site.register(AnswerSheet)
admin.site.register(Answer)
admin.site.register(User)
