# Create virtual environment
python -m venv django_env
source django_env/bin/activate

# Install Django
pip install django==4.2.3

# Create project
django-admin startproject mysite
cd mysite

# Create app
python manage.py startapp blog

# Apply migrations
python manage.py migrate