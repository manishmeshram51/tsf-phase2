
# tsf-
This is REST api using django.
django
django rest framework
xampp

# To copy the project, only copy the DRF_tsf

# File structure of the project.
tsf_phase2
    DRF_tsf
    |   DRF_tsf
        |   __init__.py
        |   settings.py
        |   urls.py
        |   wsgi.py
    |    
    |   myapp
        |   migrations
        |   __init__.py
        |   admin.py
        |   apps.py
        |   models.py
        |   serializers.py
        |   tests.py
        |   views.py
        |
    |   manage.py

# Install virtual environment
sudo apt install python-virtualenv

# Setup virtual environment with python 3.6+
virtualenv venv -p python3

# Install python dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run server
python manage.py runserver 8000

# Test on browser
http://localhost:8000



