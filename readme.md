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
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
Use the requirements.txt file to install all dependencies:
```bash
pip install -r requirements.txt
```

### 4. Download videos
To download videos based on the program, please download the video at the following link
```
https://drive.google.com/drive/folders/1g70uHT38XNkLRpGDH06OOACPIkex5f9q?usp=sharing
```
And put in videos folder

Or if you want to change the videos, please change the program in index.html : 
```
 const videos = [
            { "title": "9 mm_go_bang", "url": "/videos/9 mm_go_bang.mp4", "thumbnail": "https://picsum.photos/300/200?random=1", "video_info": "video 1" },
            { "title": "biasphemous", "url": "/videos/blasphemous.mp4", "thumbnail": "https://picsum.photos/300/200?random=2", "video_info": "video 2" },
            { "title": "fate", "url": "/videos/fate.mp4", "thumbnail": "https://picsum.photos/300/200?random=3", "video_info": "video 3" },
            { "title": "fate2", "url": "/videos/fate2.mp4", "thumbnail": "https://picsum.photos/300/200?random=4", "video_info": "video 4" },
            { "title": "The_lost_soul", "url": "/videos/The_lost_soul.mp4", "thumbnail": "https://picsum.photos/300/200?random=5", "video_info": "video 5" }
        ];
```

Change code above base on your videos. 
### 5. Run the Application
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
Open your browser and go to:
```
http://127.0.0.1:8000
```

After that, 

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
└── Videos
```
