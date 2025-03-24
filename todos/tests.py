from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo
from django.contrib.auth.models import User

class TodoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.todo_data = {'title': 'Test Todo', 'completed': False}

    def test_create_todo(self):
        response = self.client.post(reverse('todo-list'), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test Todo')

    def test_get_todo_list(self):
        self.client.post(reverse('todo-list'), self.todo_data)
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_todo(self):
        todo = Todo.objects.create(**self.todo_data)
        response = self.client.patch(reverse('todo-detail', args=[todo.id]), {'completed': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo.refresh_from_db()
        self.assertTrue(todo.completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(**self.todo_data)
        response = self.client.delete(reverse('todo-detail', args=[todo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)