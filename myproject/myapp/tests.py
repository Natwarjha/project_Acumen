
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class ApiAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_greet_user(self):
        response = self.client.get(reverse('greet'), {'name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello John'})

    def test_process_form(self):
        response = self.client.post(reverse('process_form'), {'name': 'John', 'age': 30, 'salary': 5000})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John is 30 years old and earns 5000.00 every month.')

    def test_fetch_jokes(self):
        response = self.client.post(reverse('fetch_jokes'), {'count': 3})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/jokes.html')

