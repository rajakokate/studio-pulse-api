from django.test import TestCase
from django.urls import reverse

class HealthCheckTest(TestCase):
    def test_health_check(self):
        response = self.client.get(reverse('health-check'))  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})  # Expected response


class DepartmentTest(TestCase):
    def test_create_department(self):
        response = self.client.post('departments/',
        {
            'deptId': 'D001',
            'deptName': 'COMP',
            'description' : 'I'
        }, content_type='json')
        print("response ::::::::::,",response)
        self.assertEqual(response.status_code, 201)  

import json

class UserTest(TestCase):
    def test_create_user(self):
        data = {
            'userName': 'John Doe',
            'dept': 'C001',
            'userId': 'U123',
            'contact': '9876543210',
            'email': 'john@example.com'
        }
        response = self.client.post(
            '/users/',
            data=json.dumps(data),
            content_type='json'
        )
        self.assertEqual(response.status_code, 201)






        



