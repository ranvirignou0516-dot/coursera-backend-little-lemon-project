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