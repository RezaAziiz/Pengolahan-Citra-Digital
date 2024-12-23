# Web Video Player Control Using Hand Gesture Recognition (MediaPipe)

This project implements a real-time hand gesture recognition system to control a web video player. Using **MediaPipe** and **OpenCV**, users can interact with video playback functionalities like play, pause, volume adjustment, and video navigation through intuitive hand gestures. 

The system promotes a **touchless experience** and is particularly useful in scenarios where physical interaction with devices is limited.

---

## Features

- **Real-time Gesture Recognition**: Control video player using predefined hand gestures.
- **Touchless Video Player Control**: Play, pause, adjust volume, or switch videos without physical contact.
- **MediaPipe Integration**: Use MediaPipe for accurate hand gesture detection and tracking.
- **Web-Based Video Player**: Developed using **HTML5** and **JavaScript** for dynamic and responsive video control.

---

## Requirements

Ensure you have the following installed:
- Python 3.7 or higher
- `pip` (Python Package Manager)
- OpenCV
- MediaPipe
- Web Browser (Google Chrome recommended)
- Webcam / Camera for gesture input

---

## Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/RezaAziiz/hand-gesture-video-player.git
cd hand-gesture-video-player
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
            { "title": "Manuk Dadali 1", "url": "/videos/Manuk Dadali 1.mp4", "thumbnail": "https://picsum.photos/300/200?random=1", "video_info": "video 1" },
            { "title": "Manuk Dadali 2", "url": "/videos/Manuk Dadali 2.mp4", "thumbnail": "https://picsum.photos/300/200?random=2", "video_info": "video 2" },
            { "title": "Manuk Dadali 3", "url": "/videos/Manuk Dadali 3.mp4", "thumbnail": "https://picsum.photos/300/200?random=3", "video_info": "video 3" },
            { "title": "Cendol Dawet 1", "url": "/videos/Cendol Dawet 1.mp4", "thumbnail": "https://picsum.photos/300/200?random=1", "video_info": "video 4" },
            { "title": "Cendol Dawet 2", "url": "/videos/Cendol Dawet 2.mp4", "thumbnail": "https://picsum.photos/300/200?random=2", "video_info": "video 5" },
            { "title": "Cendol Dawet 3", "url": "/videos/Cendol Dawet 3.mp4", "thumbnail": "https://picsum.photos/300/200?random=3", "video_info": "video 6" },
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

After that, open the program
```python
python .\handsControl.py
``` 

Then website and webcam gonna open. 

## IMPORTANT
After website appear, please click the content in website and after that you can use the program 
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

---

## Demo & Documentation

- **Journal Link**: [Click here to access the journal](https://drive.google.com/file/d/10pGic2PxJHp-ZC7FHzxsLUd0dUeIcnLR/view?usp=sharing) <!-- Replace # with the actual journal link -->
- **Live Demo**: [Watch the demo here](https://youtu.be/FEXXOp4Cw4w) <!-- Replace # with the actual demo link -->

---

## Contributors

- **Mahardika Pratama** (221524044)
- **Mochamad Fathur Rabbani** (221524045)
- **Reza Maulana Aziiz** (221524057)

---
