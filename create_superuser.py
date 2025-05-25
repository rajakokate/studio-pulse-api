import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studiopulse_api.settings")  # Replace with your project's settings module
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    email = "studiopulse@gmail.com"
    password = "Welcome123456"
    username = "studiopulse"

    # Create superuser without manually setting fields
    User.objects.create_superuser(username=username,email=email, password=password, is_staff=True, is_superuser=True, is_active=True)

    print(f"Superuser created successfully: {email}")

def get_all_users():
    users = User.objects.all().values_list("email", flat=True)
    print("All registered users:")
    for user_email in users:
        print(user_email)

if __name__ == "__main__":
    create_superuser()
    get_all_users()