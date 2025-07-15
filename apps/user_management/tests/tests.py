from django.test import TestCase
from django.urls import reverse

class HealthCheckTest(TestCase):
    def test_health_check(self):
        response = self.client.get(reverse('health-check'))  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})  # Expected response

from django.test import TestCase, Client
from django.urls import reverse
from .models import Department  # Adjust the import if needed

class CreateDepartmentViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_create_department_view(self):
        """
        Test GET request returns the department creation page.
        """
        response = self.client.get(reverse('create-department'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_department.html')

    def test_post_create_department_view(self):
        """
        Test POST request creates a department and renders success context.
        """
        data = {
            'deptId': 'CS01',
            'deptName': 'Computer Science'
        }
        response = self.client.post(reverse('create-department'), data)

        # Check that the Department was created
        self.assertEqual(Department.objects.count(), 1)
        department = Department.objects.first()
        self.assertEqual(department.deptId, 'CS01')
        self.assertEqual(department.deptName, 'Computer Science')

        # Check if the success flag is in context
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_department.html')
        self.assertTrue('success' in response.context)
        self.assertTrue(response.context['success'])
