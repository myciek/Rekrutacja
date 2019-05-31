from exams.models import Exercise, User, PossibleAnswer, Exam, AnswerSheet, Answer
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create_superuser(username='admin', password='admin', email='admin@gmail.com')
        teacher1 = User.objects.create_user('teacher1', 'teacher1@gmail.com', 'teacher1', is_teacher=True)
        teacher2 = User.objects.create_user('teacher2', 'teache2r@gmail.com', 'teacher2', is_teacher=True)
        student = User.objects.create_user('student', 'student@gmail.com', 'student')

        exercise1 = Exercise.objects.create(owner=teacher1, name='Ex1',
                                            text='Which method is used to create objects? ', max_points=5)
        exercise2 = Exercise.objects.create(owner=teacher1, name='Ex2',
                                            text="REST is short from: ", max_points=5, written_exercise=True)

        possible_answer1 = PossibleAnswer.objects.create(key='A', value='GET', exercise=exercise1, correct=False)
        possible_answer2 = PossibleAnswer.objects.create(key='B', value='DELETE', exercise=exercise1, correct=False)
        possible_answer3 = PossibleAnswer.objects.create(key='C', value='POST', exercise=exercise1, correct=True)
        possible_answer4 = PossibleAnswer.objects.create(key='D', value='PATCH', exercise=exercise1, correct=False)

        exam1 = Exam.objects.create(owner=teacher1, subject='Web Technologies', max_points=5)
        exam1.exercises.set(Exercise.objects.all())

        answer_sheet1 = AnswerSheet.objects.create(exam=exam1, student=student)
        answer1 = Answer.objects.create(answer_sheet=answer_sheet1, exercise=exercise1, answer=possible_answer1,
                                        points=0)
        answer2 = Answer.objects.create(answer_sheet=answer_sheet1, exercise=exercise2,
                                        written_answer="Representational State Transfer", points=5)
