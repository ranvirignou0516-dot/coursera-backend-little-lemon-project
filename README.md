# Little Lemon Backend API

## Project Overview

Little Lemon Backend API is a Django REST Framework based backend application developed as part of the Coursera Backend Developer Project.

The project provides RESTful APIs for managing restaurant menu items, table bookings, and user authentication using token-based authentication.

---

## Technology Stack

- Python 3
- Django 6.0.7
- Django REST Framework
- MySQL Database
- Djoser Authentication
- Token Authentication
- Postman / Insomnia API Testing

---

## Features

### Authentication
- User login using token authentication
- Get logged-in user details
- Token based API authorization
- Logout API

### Menu Management
- View all menu items
- View single menu item
- Create menu item
- Update menu item
- Delete menu item

### Booking Management
- View all bookings
- View single booking
- Create booking
- Update booking
- Delete booking

---

## Database Configuration

This project uses MySQL database.

Database configuration example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
## Installation Steps

### 1. Clone Repository
```bash
git clone <repository-url>
```
### 2. Create Virtual Environment
```bash
python -m venv venv
```
### 3. Activate Virtual Environment

Windows:
```bash
venv\Scripts\activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Run Database Migration
```bash
python manage.py migrate
```
### 6. Create Superuser
```bash
python manage.py createsuperuser
```
### 7. Start Development Server
```bash
python manage.py runserver
```
## Base URL

Local Development:
```text
http://127.0.0.1:8000/
```
## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | /auth/token/login/ | Login and generate token |
| GET | /auth/users/me/ | Current user details |

### Menu APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | /restaurant/menu/ | List menu items |
| GET | /restaurant/menu/id/ | Single menu item |
| POST | /restaurant/menu/ | Create menu |
| PUT | /restaurant/menu/id/ | Update menu |
| PATCH | /restaurant/menu/id/ | Partial update menu item |
| DELETE | /restaurant/menu/id/ | Delete menu |

### Booking APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | /restaurant/booking/ | List bookings |
| GET | /restaurant/booking/id/ | Single booking |
| POST | /restaurant/booking/ | Create booking |
| PUT | /restaurant/booking/id/ | Update booking |
| PATCH | /restaurant/booking/id/ | Partial update booking|
| DELETE | /restaurant/booking/id/ | Delete booking |

---

## Authentication Header

Protected APIs require token authentication.

Example:
```http
Authorization: Token your_token_here
```
## API Testing

The APIs were tested using:

-Postman
-Insomnia

Tested operations:

- Authentication
- Menu CRUD operations
- Booking CRUD operations

## Project Structure

```text
Little Lemon Backend Project

├── littlelemon
│   ├── settings.py
│   ├── urls.py
│
├── restaurant
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```
## Author

Ranvir Kumar
