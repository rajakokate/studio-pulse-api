# studiopulse
StudioPulse is an offline desktop application for media project tracking and file path management. Built using React, Django REST Framework, and Electron, it enables teams to collaborate efficiently, track assets, and manage local files within structured project workflows.


# Add permission
1) Create superuser for application
    python manage.py createsuperuser
    - Enter the details:  (we can enter anything)
      - Username: studio-pulse
      - email - studio.pulse@gmail.com
      - password: Welcome
2) start the server - python manage.py runserver (Assume all the migrations are already done)
2) Get the token -  Using postman
  POST: http://127.0.0.1:8000/studio-pulse/login/
    {
        "username": "studio-pulse",
        "password": "Welcome123456"
    }
3) Add the permission 
   - Capture the token from step 2 and 
   - click on Authorization section on postman
   - select bearer token and paste the token in Token section
   - on request type selection select post and
   - localhost:8000/studio-pulse/api/permissions/
   to create permission of type everything, paste the below in Body section in postman
   {
    "codename": "ALL",
    "name": "ALL",
    "content_type": 1  
   }
4) click on send to create permission, we can create other permission like this
5) Add the user group
    - We again need to use the token as suggested in step 3
    - POST on localhost:8000/studio-pulse/api/groups/
    - body
     {
       "name": "Admin"
    }
   
6) now user can register using the below
    - POST - localhost:8000/studio-pulse/register/
    - body
    {
    "username": "user1Name",
    "contact": "8763848224",
    "email": "user1.lastname@gmail.com",
    "role": "Lead",
    "dept": "CSE001",
    "password": "Welcome123456",
    "password2": "Welcome123456",
    "groups": [1],
    "user_permissions": [1]
  }
7) login
    