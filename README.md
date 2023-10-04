# Fused CRM

This is a repository for a web application developed with Django, built with [fused](https://github.com/fseanwork08/fused_python_backend)

## Table of Contents

1. [Project Structure](#project-structure)
2. [Features](#features)
3. [Getting Started: Backend](#getting-started-backend)
4. [Usage](#usage)
   - [Admin Panel](#admin-panel)
   - [API Documentation](#api-documentation)

## Project Structure

    ..
    ├── crm                            # Starter home app
    ├── fused                          # fused Modules app
    ├── fused                          # Django project configurations
    ├── static                         # Static assets
    ├── users                          # Starter users app
    ├── templates                      # html templates
    ├── ...
    ├── README.md
    └── ...

## Features

1. **Local Authentication** using email and password with [allauth](https://pypi.org/project/django-allauth/)
2. **Rest API** using [django rest framework](http://www.django-rest-framework.org/)

# Getting Started: Backend

Following are instructions on setting up your development environment.

The recommended way for running the project locally and for development is using virtualenv.

## Local Setup (Alternative to Docker)

1. [MYSQL](https://dev.mysql.com/downloads/installer/)
2. [Python](https://www.python.org/downloads/release/python-386/)

### Installation

1. Install [pipenv](https://pypi.org/project/pipenv/)
2. Clone this repo and `cd fused_python_backend`
3. Run `pip3 install -r requirements.txt` to get the latest pipenv version.
4. Run `cp .env.example .env`
5. Update .env file `DATABASE_URL` with your `database_name`, `database_user`, `database_password`, if you use postgresql.
   Can alternatively set it to `sqlite:////tmp/my-tmp-sqlite.db`, if you want to use sqlite for local development.

### Getting Started

1. Run `python manage.py makemigrations`
2. Run `python manage.py migrate`
3. Run `python manage.py runserver`

# Usage

## Admin Panel

Admin Panel can be accessed through http://localhost:8000/admin/. 
## API Documentation

API Documentation is generated automatically and can be access through http://localhost:8000/api-docs/.
