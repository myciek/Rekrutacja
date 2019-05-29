# from django.urls import path
# from exams import views
#
# urlpatterns = [
#     path('exercises/', views.ExerciseList.as_view(), name='exercises'),
#     path('possible_answers/', views.PossibleAnswerList.as_view(), name='possible_answers'),
#     path('answer_sheets/', views.AnswerSheetList.as_view(), name='answer_sheets'),
#     path('exams/', views.ExerciseList.as_view(), name='exams'),
#     path('answers/', views.AnswerList.as_view(), name='answers'),
#
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exams import views

router = DefaultRouter()
router.register('exercises', views.ExerciseViewSet)
router.register('possible_answers', views.PossibleAnswerViewSet)
router.register('exams', views.ExamViewSet)
router.register('answer_sheets', views.AnswerSheetViewSet)
router.register('answers', views.AnswerViewSet)

app_name = 'exam'

urlpatterns = [
    path('', include(router.urls))
]