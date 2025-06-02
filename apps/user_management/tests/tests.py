from django.test import TestCase
from django.urls import reverse

class HealthCheckTest(TestCase):
    def test_health_check(self):
        response = self.client.get(reverse('health-check'))  # Make sure this URL exists in your app
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})  # Expected response