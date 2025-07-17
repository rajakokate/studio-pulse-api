from django.test import TestCase
from rest_framework.test import APIClient
from apps.user_management.models import User
from apps.task_management.models import Shot, ShotAssociation, Project

class ArtistShotStatsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create artist and lead user
        self.artist = User.objects.create_user(
            username='test_artist',
            email='test@gmail.com',
            password='testpass'
        )
        self.lead = User.objects.create_user(
            username='test_lead',
            email='lead@example.com',
            password='leadpass'
        )

        self.client.force_authenticate(user=self.artist)

        # Create project
        self.project = Project.objects.create(
            projectName="Test Project",
            status="TODO"
        )

        # Create and assign shots
        shot1 = Shot.objects.create(
            shotId=1,
            Status="APPROVED",
            ProjectId=self.project
        )
        ShotAssociation.objects.create(
            shot=shot1,
            user=self.artist,
            version=1.0
        )

        shot2 = Shot.objects.create(
            shotId=2,
            Status="IN PROGRESS",
            ProjectId=self.project
        )
        ShotAssociation.objects.create(
            shot=shot2,
            user=self.artist,
            version=2.0
        )

        shot3 = Shot.objects.create(
            shotId=3,
            Status="TODO",
            ProjectId=self.project
        )
        ShotAssociation.objects.create(
            shot=shot3,
            user=self.artist,
            version=1.5
        )

        shot4 = Shot.objects.create(
            shotId=4,
            Status="IN REVIEW",
            ProjectId=self.project
        )
        ShotAssociation.objects.create(
            shot=shot4,
            user=self.lead,                 # Lead is the reviewer
            assigned_from=self.artist,      # Artist assigned it for review
            version=3.0
        )

    def test_artist_shot_statistics(self):
        response = self.client.get('/studio-pulse/stats/artist-shots/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['completed'], 1)
        self.assertEqual(response.data['in_progress'], 1)
        self.assertEqual(response.data['todo_assigned'], 1)
        self.assertEqual(response.data['in_review'], 1)