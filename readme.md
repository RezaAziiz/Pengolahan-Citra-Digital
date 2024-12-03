# Video Streaming and Player Web Application

A simple web application built with FastAPI for video streaming and video player functionality. The project uses Jinja2 templates for rendering dynamic content and OpenCV for image processing.

## Features
- Video player with dynamic content.
- Video thumbnail rendering using OpenCV.
- Modern responsive design using Tailwind CSS.
- Built-in video switching functionality.

---

## Requirements
Make sure you have the following installed:
- Python 3.7 or higher
- `pip` (Python package manager)

---

## Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/RezaAziiz/Pengolahan-Citra-Digital.git
cd Pengolahan-Citra-Digital
```

### 2. Set up a virtual environment
It's recommended to use a virtual environment to avoid dependency conflicts:
```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install dependencies
Use the requirements.txt file to install all dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
Open your browser and go to:
```
http://127.0.0.1:8000
```

---

## Folder Structure
```
Pengolahan-Citra-Digital/
│
├── main.py                # Main FastAPI application
├── templates/  
|──── index.html           
├── requirements.txt       # List of dependencies
└── README.md
```
