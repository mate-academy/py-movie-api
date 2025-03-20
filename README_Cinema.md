# Steps taken to build the Cinema project

## Initial Ubuntu VM Setup (not required)

- Follow the instruction from this [README](https://github.com/mcspidy/knowely_django/blob/main/README.md) file .

## Setup for the project

1. Create the `.gitignore` file, at a minimum with the following

    ```text
    .vscode/
    .DS_Store
    venv/
    .pytest_cache/
    __pycache__/
    *.pyc
    db.sqlite*
    ```

2. Create the `requirements.txt` file
    - add/remove packages as necessary

        ```text
        crispy_bootstrap4==2024.10
        black==25.1.0
        django==5.1.5
        django-debug-toolbar==5.0.1
        django-crispy-forms==2.3
        django-extensions==3.1.3
        djangorestframework==3.15.2
        flake8==7.1.1
        flake8-quotes==3.4.0
        flake8-variables-names==0.0.6
        pep8-naming==0.13.2
        ```

3. Run the following commands in a terminal to build the environment
    - On a Ubuntu Server 24.04

        ```bash
        python -m venv venv
        source venv/bin/activate
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        ```

4. Prepare Django app

    ```bash
    django-admin startproject app . 
    ```

5. Create folders

    ```bash
    mkdir cinema/
    mkdir cinema/migrations/
    mkdir tests/
    ```

6. Create empty `__init__.py` files

    ```bash
    touch cinema/__init__.py
    touch cinema/migrations/__init__.py
    ```

7. Load Data

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata cinema_service_db_data.json
    ```

8. Teat file

    - Create `test_cinema_app.py`

        ```bash
        touch tests/test_cinema_app.py
        ```

    - Execute the following to add a few import lines

        ```bash
        echo -e "from django.core.exceptions import ValidationError\nfrom django.db import IntegrityError" >> tests/test_cinema_app.py
        echo -e "from django.contrib.auth import get_user_model\nfrom django.test import TestCase\nfrom django.urls import reverse" >> tests/test_cinema_app.py
        ```

    - Create test class and functions

    - Run the test

        ```bash
        python manage.py test
        ```
