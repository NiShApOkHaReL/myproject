# Parking Management System with ANPR


## Overview

This project is a comprehensive parking management system that utilizes Automatic Number Plate Recognition (ANPR) technology to manage and monitor parking spaces. The system is designed to automate the process of vehicle identification, parking space allocation, and overall parking management.


## Features

- **Automatic Number Plate Recognition (ANPR)**: Efficiently reads and processes vehicle number plates using state-of-the-art image processing techniques.
- **Real-time Monitoring**: View available parking spaces and track parking status in real-time.
- **Database Integration**: Store and manage parking records, including vehicle information and parking history.
- **User Interface**: Intuitive web-based interface for both administrators and users.
- **Image Processing**: Handles image uploads, resizing, and storage for ANPR and other functionalities.
- **Migration Support**: Database migrations to handle schema changes seamlessly.
  

## Technologies Used

- **Backend**: Python with Django framework
- **Database**: SQLite
- **ANPR**: YOLOv9 for license plate detection and eacyOCR for character recognization
- **Frontend**: HTML, CSS
  

## Installation

### Prerequisites

- Python 3.x
- Django
- OpenCV
- Other dependencies listed in `requirements.txt` inside yolov9 folder

### Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/NiShApOkHaReL/myproject.git

   ```
   cd myproject

  ```
  python manage.py migrate

  ```
  python manage.py runserver


2. **Open your browser and go to http://127.0.0.1:8000 to view the application.**

 
 
