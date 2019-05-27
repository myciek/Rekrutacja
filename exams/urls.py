from django.urls import path
from exams import views

urlpatterns = [
    path('exercises/', views.ExerciseList.as_view(), name='exercises'),
    path('possible_answers/', views.PossibleAnswerList.as_view(), name='possible_answers'),
    path('answer_sheets/', views.AnswerSheetList.as_view(), name='answer_sheets'),
    path('exams/', views.ExerciseList.as_view(), name='exams'),
    path('answers/', views.AnswerList.as_view(), name='answers'),

]

