#StudioPulse - Django REST API

StudioPulse is a full-stack web application built  with Django REST Framework (DRF for backend and PostgreSQL as the database). This project manages client studio  operations including user management, shot assignment, project preview and review dashboard.

## Tech Stack
-**Backend** : Django, Django REST Framework
<!-- -**Database** PostgreSQL --> (optional)
-**Frontend** React Handled in separate repo

#### Prerequisites
- Python 3.10 or higher
<!-- - postgreSQL installed and running --> (optional)
- Git installed 

##### Clone the repository 
```bash
git clone https://github.com/rajakokate/studio-pulse-api.git
cd studio-pulse-api
```

## Project Structure
studio-pulse-api/
├── src/
│ ├── studiopulse_api/
│ │ ├── init.py --`Marks directory as a Python package`
│ │ ├── asgi.py -- `ASGI config for asynchronous support`
│ │ ├── settings.py -- `Global Django settings`
│ │ ├── urls.py -- `Root URL configurations`
│ │ ├── wsgi.py -- `WSGI config for deployment`
│ │ └── users/
│ │ ├── init.py -- `Marks users as a Python package`
│ │ ├── admin.py -- `Admin interface model registration`
│ │ ├── apps.py -- `App config class`
│ │ ├── models.py -- `Database models for the users app`
│ │ ├── seed.py -- `Script to seed initial/demo data`
│ │ ├── serializers.py -- `Converts models to/from JSON (API layer)`
│ │ ├── tests.py -- `Unit and integration tests`
│ │ ├── urls.py -- `URLs for users-related endpoints`
│ │ ├── views.py -- `Business logic for handling requests`
│ │ ├── migrations/ -- `DB migration files`
│ │ └── templates/ -- `HTML or email templates (if any)`
├── .gitignore -- `Git ignored files`
├── manage.py -- `Django CLI tool for management`
├── manage_backup.py -- `Optional backup manage script`
├── tm.sh -- `Shell script for local automation`

## File/Folder Purpose

#### `studiopulse_api`
This is the main Djanog project directory  that contains core settings and configuration

-**`__init__py`**: Initializes the python package
-**`asgi.py`**: Entry point for ASGI-compatible servers(used for handling asynchronous requests).
**`settings.py`**: contains all global project settings such as database configuration, installed apps, middleware, authentication and static files
-**`urls.py`**: Root URL dispatcher for routing incoming requests to the  appropriate app.
-**`wsgi.py`**: Entry point for WSGI-compatible servers(commonly used  in deployment )

---

#### `users/`
This is a Django app within the project that manages user-related functionality.
-**`__init__.py`**: Initializes the users app as a python module
-**`admin.py`**: Registers Django models to appear in the Django admin dashboard
-**`apps.py`**: contains the app configuration class , used by Django for app specific settings.
-**`models.py`**: Defines the database schema related to users using Django ORM.
-**`serializers.py`**: converts complex model instances to and from JSON for API requests and responses using DRF
-**`views.py`**: contains the business logic that handles HTTP requests (GET, POST, etc.) and return responses
-**`urls.py`**: Maps specific URLs to views inside the users app 
-**`tests.py`**: Unit tests and integration tests for validating the functionality of the app
-**`seed.py`**: custom script for populating the database with demo or initial data . Useful for development or testing.
-**`migrations/`**: contains Django migration files that  track changes to the database shchema


#### Project root files

-**`.gitignore`**: Specifies intentionally untracked files and directories that Git should ignore
-**`manage.py`**: A command-line utility for managing the Django project (e.g., running server, migrations).
-**`manage_backup.py`**: A backup version of `manage.py`
-**`tm.sh`**: A shell script, used for startin the project `$pyrun`


###  setup instructions

# Go to the proejct root directory  

cd studio-pulse-api

# Create and activate virtual environment
python -m venv venv 
source venv/bin/activate  `on Unix/mac`
venv\Scripts\activate   `on windows`

# Install Dependencies

pip install -r requirement.txt

## Configure Environment variables

Create a .env file in the `src` folder and add the following variables

SECRET_KEY=YOUR_SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

Note: Keep your .env file private and never push it to version control.

## Migrate the database

python manage.py makemigrations
python manage.py migrate


## run the development  server

After activating the virtual environment and completing migrations, you can start the development server

python 


















