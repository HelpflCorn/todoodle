from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='testuser')

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            task_title='test task',
            description='some decription',
            complete=False
        )

        self.assertEqual(task.user, self.user)
        self.assertEqual(task.task_title, 'test task')
        self.assertEqual(task.description, 'some decription')
        self.assertFalse(task.complete)
        self.assertIsNotNone(task.created_date)

    def test_task_str_representation(self):
        task = Task.objects.create(
            user=self.user,
            task_title='test task 2',
            description='this is another test task.',
            complete=True
        )

        self.assertEqual(str(task), 'test task 2')