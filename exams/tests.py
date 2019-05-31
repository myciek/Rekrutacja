from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from exams.models import Exercise, User, PossibleAnswer, Exam, AnswerSheet, Answer

from exams.serializers import ExerciseSerializer, PossibleAnswerSerializer, ExamSerializer, AnswerSheetSerializer, \
    AnswerSerializer


class AuthorizeTests(TestCase):
    # access to exercises when unauthorized

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get('http://localhost:8000/exercises/')

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class ExerciseTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user('test', 'test@gmail.com', 'testpass')
        self.teacher = User.objects.create_user('teacher', 'teacher@gmail.com', 'teacherpass', is_teacher=True)
        self.other_teacher = User.objects.create_user('teacher2', 'teache2r@gmail.com', 'teacherpass', is_teacher=True)
        self.client = APIClient()

    def test_get_exercise(self):
        self.client.force_authenticate(self.teacher)
        Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)
        Exercise.objects.create(owner=self.teacher, name='test_exercise2', text='1234', max_points=5)

        res = self.client.get('http://localhost:8000/exercises/')
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_get_exercise_as_student(self):
        self.client.force_authenticate(self.student)
        Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)
        Exercise.objects.create(owner=self.teacher, name='test_exercise2', text='1234', max_points=5)

        res = self.client.get('http://localhost:8000/exercises/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_exercise_bad_parameters(self):
        self.client.force_authenticate(self.teacher)
        data = {'name': 'test_exercise3', 'text': '123'}
        res = self.client.post('http://localhost:8000/exercises/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_exercise_as_owner(self):
        self.client.force_authenticate(self.teacher)
        exercise = Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)

        res = self.client.delete('http://localhost:8000/exercises/' + str(exercise.id) + '/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_exercise_as_other(self):
        self.client.force_authenticate(self.other_teacher)
        exercise = Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)

        res = self.client.delete('http://localhost:8000/exercises/' + str(exercise.id) + '/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PossibleAnswersTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user('test', 'test@gmail.com', 'testpass')
        self.teacher = User.objects.create_user('teacher', 'teacher@gmail.com', 'teacherpass', is_teacher=True)
        self.client = APIClient()

    def test_get_possible_answer(self):
        self.client.force_authenticate(self.teacher)
        test_exercise = Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)
        PossibleAnswer.objects.create(key='A', value='Test', exercise=test_exercise, correct=True)

        res = self.client.get('http://localhost:8000/possible_answers/')
        possible_answers = PossibleAnswer.objects.all()
        serializer = PossibleAnswerSerializer(possible_answers, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_get_possible_answer_as_student(self):
        self.client.force_authenticate(self.student)
        test_exercise = Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)
        PossibleAnswer.objects.create(key='A', value='Test', exercise=test_exercise, correct=True)

        res = self.client.get('http://localhost:8000/possible_answers/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_possible_answer(self):
        self.client.force_authenticate(self.teacher)
        test_exercise = Exercise.objects.create(owner=self.teacher, name='test_exercise', text='123', max_points=5)
        data = {'key': 'A', 'value': 'Test', 'exercise': test_exercise.id, 'is_correct': True}

        res = self.client.post('http://localhost:8000/possible_answers/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_possible_answer_bad_parameters(self):
        self.client.force_authenticate(self.teacher)
        data = {'name': 'test_exercise3', 'text': '123'}
        res = self.client.post('http://localhost:8000/possible_answers/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class ExamTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user('test', 'test@gmail.com', 'testpass')
        self.teacher = User.objects.create_user('teacher', 'teacher@gmail.com', 'teacherpass', is_teacher=True)
        self.other_teacher = User.objects.create_user('teacher2', 'teache2r@gmail.com', 'teacherpass', is_teacher=True)
        self.client = APIClient()

    def test_get_exam(self):
        self.client.force_authenticate(self.teacher)
        Exam.objects.create(owner=self.teacher, subject='Testing', max_points=5)

        res = self.client.get('http://localhost:8000/exams/')
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_get_exam_as_student(self):
        self.client.force_authenticate(self.student)
        Exam.objects.create(owner=self.teacher, subject='Testing', max_points=5)

        res = self.client.get('http://localhost:8000/exams/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_exam_bad_parameters(self):
        self.client.force_authenticate(self.teacher)
        data = {'name': 'test_exercise3', 'text': '123'}
        res = self.client.post('http://localhost:8000/exams/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_exam_as_owner(self):
        self.client.force_authenticate(self.teacher)
        exam = Exam.objects.create(owner=self.teacher, subject='Testing', max_points=5)

        res = self.client.delete('http://localhost:8000/exams/' + str(exam.id) + '/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_exam_as_other(self):
        self.client.force_authenticate(self.other_teacher)
        exam = Exam.objects.create(owner=self.teacher, subject='Testing', max_points=5)

        res = self.client.delete('http://localhost:8000/exams/' + str(exam.id) + '/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AnswersSheetTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user('test', 'test@gmail.com', 'testpass')
        self.client = APIClient()

    def test_get_answer_sheet(self):
        self.client.force_authenticate(self.student)
        test_exam = Exam.objects.create(owner=self.student, subject='Testing', max_points=5)
        AnswerSheet.objects.create(exam=test_exam, student=self.student)

        res = self.client.get('http://localhost:8000/answer_sheets/')
        answer_sheets = AnswerSheet.objects.all()
        serializer = AnswerSheetSerializer(answer_sheets, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_create_answer_sheet(self):
        self.client.force_authenticate(self.student)
        test_exam = Exam.objects.create(owner=self.student, subject='Testing', max_points=5)
        data = {'exam': test_exam.id, 'student': self.student.id, 'points': 0, 'grade': 2}

        res = self.client.post('http://localhost:8000/answer_sheets/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_answer_sheet_bad_parameters(self):
        self.client.force_authenticate(self.student)
        data = {'name': 'test_exercise3', 'text': '123'}
        res = self.client.post('http://localhost:8000/answer_sheets/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class AnswersTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user('test', 'test@gmail.com', 'testpass')
        self.client = APIClient()

    def test_get_answer(self):
        self.client.force_authenticate(self.student)
        test_exercise = Exercise.objects.create(owner=self.student, name='test_exercise', text='123', max_points=5)
        test_exam = Exam.objects.create(owner=self.student, subject='Testing', max_points=5)
        test_answer = PossibleAnswer.objects.create(key='A', value='Test', exercise=test_exercise, correct=True)
        test_answer_sheet = AnswerSheet.objects.create(exam=test_exam, student=self.student)

        Answer.objects.create(answer_sheet=test_answer_sheet, exercise=test_exercise, answer=test_answer, points=2)

        res = self.client.get('http://localhost:8000/answers/')
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_create_answer(self):
        self.client.force_authenticate(self.student)
        test_exercise = Exercise.objects.create(owner=self.student, name='test_exercise', text='123', max_points=5)
        test_exam = Exam.objects.create(owner=self.student, subject='Testing', max_points=5)
        test_answer = PossibleAnswer.objects.create(key='A', value='Test', exercise=test_exercise, correct=True)
        test_answer_sheet = AnswerSheet.objects.create(exam=test_exam, student=self.student)
        data = {'answer_sheet': test_answer_sheet.id, 'exercise': test_exercise.id, 'answer': test_answer.id, 'points': 2}

        res = self.client.post('http://localhost:8000/answers/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_answer_bad_parameters(self):
        self.client.force_authenticate(self.student)
        data = {'name': 'test_exercise3', 'text': '123'}
        res = self.client.post('http://localhost:8000/answers/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
