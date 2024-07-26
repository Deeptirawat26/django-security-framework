# Django Security Framework for File Upload and Encryption

## Introduction
This project is a Django-based security framework for file upload and encryption. It provides user-defined file access, allowing users to upload files, which are then encrypted for secure storage and can be decrypted when needed.

## Features
- **User Registration and Login:** Secure user authentication system.
- **File Upload via Form:** Users can upload files through a web form.
- **File Encryption and Decryption:** Uploaded files are encrypted for secure storage and can be decrypted by authorized users.
- **Logs in Admin Panel:** Admins can view logs of user activities and file operations.

## Pre-Requisites
Ensure you have the following installed on your system:
- Python (version 3.6 or higher)
- Django (version 3.x or higher)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Deeptirawat26/django-security-framework

2. **Deployment:**
   ```bash
   python manage.py runserver

## Usage

Register a new user: Navigate to http://127.0.0.1:8000/register/ and register a new account.

Login: Go to http://127.0.0.1:8000/login/ and log in with your account.

Upload a file: Once logged in, use the file upload form to upload your file.

View logs (Admin only): Log in to the admin panel at http://127.0.0.1:8000/admin/ with the superuser account to view logs.

