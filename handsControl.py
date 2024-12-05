import cv2
import numpy as np
import HandTrackingDynamic as htd
import time
import pyautogui
import math
from selenium import webdriver  # Used to interact with the HTML page

# Configuration parameters
wVideo = 640
hVideo = 480
ctime = 0
ptime = 0
wScr, hScr = pyautogui.size()  # Screen size
frameR = 100  # Frame Reduction
smoothing = 7  # Smoothing factor for mouse movement
xloc, yloc = 0, 0  # Previous x and y positions for smoothing
clocx, clocy = 0, 0  # Current x and y positions

# Setup for video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, wVideo)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hVideo)
detector = htd.HandTrackingDynamic(maxHands=1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Setup a simple Selenium WebDriver to control the video player
driver = webdriver.Chrome()  # Assuming Chrome driver is installed
driver.get(" http://127.0.0.1:8000")

# Function to trigger video controls through the HTML page
def control_video(action):
    if action == "play_pause":
        driver.execute_script('document.querySelector("#video-player").paused ? document.querySelector("#video-player").play() : document.querySelector("#video-player").pause();')
    elif action == "volume_up":
        driver.execute_script('document.querySelector("#video-player").volume = Math.min(document.querySelector("#video-player").volume + 0.1, 1);')
    elif action == "volume_down":
        driver.execute_script('document.querySelector("#video-player").volume = Math.max(document.querySelector("#video-player").volume - 0.1, 0);')
    elif action == "mute":
        driver.execute_script('document.querySelector("#video-player").muted = !document.querySelector("#video-player").muted;')
    elif action == "seek_forward":
        driver.execute_script('document.querySelector("#video-player").currentTime += 10;')
    elif action == "seek_backward":
        driver.execute_script('document.querySelector("#video-player").currentTime -= 10;')

# Function to detect gestures and map them to video controls
def detect_gestures_and_control(lmsList):
    if len(lmsList) == 0:
        return
    
    # Check if the fist gesture (all fingers closed) is detected for Play/Pause
    if all(lmsList[i][2] < lmsList[i-1][2] for i in [4, 8, 12, 16, 20]):  # Example condition for fist gesture
        control_video("play_pause")
        print("Play/Pause Gesture Detected")
    
    # Check if hand open gesture is detected for mute/unmute
    elif all(lmsList[i][2] > lmsList[i-1][2] for i in [4, 8, 12, 16, 20]):  # Example condition for open hand
        control_video("mute")
        print("Mute/Unmute Gesture Detected")
    
    # Check if index and middle fingers are pointing up for seeking forward (swipe gesture)
    elif lmsList[8][2] < lmsList[6][2] and lmsList[12][2] < lmsList[10][2]:
        control_video("seek_forward")
        print("Seek Forward Gesture Detected")
    
    # Check if the hand is swiping down for volume down
    elif lmsList[8][2] > lmsList[6][2] and lmsList[12][2] > lmsList[10][2]:
        control_video("volume_down")
        print("Volume Down Gesture Detected")
    
    # Check if the hand is swiping up for volume up
    elif lmsList[8][2] < lmsList[6][2] and lmsList[12][2] > lmsList[10][2]:
        control_video("volume_up")
        print("Volume Up Gesture Detected")

# Main loop for hand gesture detection and video control
while True:
    ret, frame = cap.read()
    frame = detector.findFingers(frame)
    lmsList, bbox = detector.findPosition(frame)

    if len(lmsList) != 0:
        detect_gestures_and_control(lmsList)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
