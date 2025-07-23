from apps.task_management.models import Project
from rest_framework.test import APITestCase # for testing API endpoints
from django.urls import reverse #to resolve endpoint URLs
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone
from apps.task_management.models import ProjectComment



class DeadlineCommentsAPITestCase(APITestCase): #group all tests related to deadline-comments

    @classmethod    
    def setUpTestData(cls):
        User = get_user_model()
        cls.user_password = "testpass123"

        #Create a test user only once
        cls.user = User.objects.create_user(
            username = "testuser",
            email = "testuser@gmail.com",
            password = cls.user_password

        )

    def setUp(self):
        #forcefull login
        self.client.force_login(self.user)
        

    def test_deadline_comments_api(self):
        
        #Step 1: Create a project  with due date within 3 days
        due_date = timezone.now() + timedelta(days=2) #near deadline
        self.project = Project.objects.create(
            projectName=  "Team Deadline Project",
            status= "IN PROGRESS",
            dueDate= due_date,
            startDate= timezone.now(),
            clientID= None,
            # dept="1",
            description="This is a test project for deadline comment filtering",
        )

        # self.project.refresh_from_db()


        #Step2: Create a comment associated with the project
        ProjectComment.objects.create(
            project = self.project, # link comment to test project
            user = self.user,
            comment= "This is a Test Comment" #Content of the comment
        )

        #step3A: GET response from the API
        url = reverse('deadline-comments') #resolve url for the endpoint
        response = self.client.get(url) #make a get request to the endpoint

        #step3B Assert response status code
        self.assertEqual(response.status_code,200) # ensure the API returns 200 OK
        self.assertGreater(len(response.data), 0)

        #step3 Validate the comment and project ID
        comment_data = response.data[0]
        self.assertEqual(comment_data['project'], str(self.project.projectID))
        self.assertEqual(comment_data['comment'] ,"This is a Test Comment")
        self.assertEqual(comment_data['user'] , self.user.email)


