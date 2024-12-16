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
detector = htd.HandTrackingModule(detectionCon=0.75, trackCon=0.75)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Setup a simple Selenium WebDriver to control the video player
driver = webdriver.Chrome()  # Assuming Chrome driver is installed
driver.get("http://127.0.0.1:8000")


# Function to trigger video controls through the HTML page
def control_video(action):
    if action == "play_pause":
        print("play_pause")
        driver.execute_script('document.querySelector("#video-player").paused ? document.querySelector("#video-player").play() : document.querySelector("#video-player").pause();')
    elif action == "volume_up":
        print("volume_up")
        driver.execute_script('document.querySelector("#video-player").volume = Math.min(document.querySelector("#video-player").volume + 0.2, 1);')
    elif action == "volume_down":
        print("volume_down")
        driver.execute_script('document.querySelector("#video-player").volume = Math.max(document.querySelector("#video-player").volume - 0.2, 0);')
    elif action == "mute_unmute_video":
        print("mute_unmute_video")
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'code': 'KeyM'}));")
    elif action == "next_video":
        print("next_video")
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'code': 'KeyN'}));")
    elif action == "prev_video":
        print("prev_video")
        driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'code': 'KeyP'}));")

# Function to detect gestures and map them to video controls
tipIds = [4, 8, 12, 16, 20]
display_message = ""
def detect_gestures_and_control(lmsList):
    global ptime,display_message  # To store the previous time for control

    # Define the left and right boxes for control (Move this part before the rectangles)
    left_box = (50, 150, 200, 300)  # (x1, y1, x2, y2) for the left box
    right_box = (440, 150, 590, 300)  # (x1, y1, x2, y2) for the right box

    # Draw the colored boxes on the screen
    cv2.rectangle(frame, (left_box[0], left_box[1]), (left_box[2], left_box[3]), (255, 0, 0), 2)  # Blue box for Next
    cv2.rectangle(frame, (right_box[0], right_box[1]), (right_box[2], right_box[3]), (0, 0, 255), 2)  # Red box for Prev

    if len(lmsList) == 0:
        return

    current_time = time.time()  # Get the current time
    
    fingers = []
        # Thumb
    if lmsList[tipIds[0]][1] > lmsList[tipIds[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
        # 4 Fingers
    for id in range(1, 5):
        if lmsList[tipIds[id]][2] < lmsList[tipIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0) 
    # Only process if enough time has passed since the last control (prevent rapid switching)
    if current_time - ptime > 2:  # 2-second delay before the next action is allowed
        ptime = current_time  # Update the previous time
        
        all_equal_to_one = all(x == 1 for x in fingers)
        two_finger = fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0 and all(x == 0 for x in fingers[3:])
        only_thumbs = fingers[0] == 1 and all(x == 0 for x in fingers[1:])
        only_kelingking = fingers[-1] == 1 and all(x == 0 for x in fingers[:-1])

        if all_equal_to_one:
            control_video("play_pause")
            display_message = "Play/Pause Video"
        elif two_finger:
            control_video("mute_unmute_video")
            display_message = "Mute/Unmuted Video"       
        elif only_thumbs:
            control_video("volume_up")
            display_message = "Volume Up Video"
        elif only_kelingking:  
            control_video("volume_down")
            display_message = "Volume Down Video"


        # Get the x-coordinate of the index finger (lmsList[8][1])
        index_x = lmsList[8][1]
        index_y = lmsList[8][2]

        

        # Check if the index finger is within the left box for Next Video
        if left_box[0] < index_x < left_box[2] and left_box[1] < index_y < left_box[3]:
            control_video("next_video")
            display_message = "Next Video Gesture Detected"

        # Check if the index finger is within the right box for Previous Video
        elif right_box[0] < index_x < right_box[2] and right_box[1] < index_y < right_box[3]:
            control_video("prev_video")
            display_message = "Previous Video Gesture Detected"

        

while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmsList = detector.findPosition(frame, draw=False)

    if len(lmsList) != 0:
        detect_gestures_and_control(lmsList)
    
       # Tampilkan pesan pada frame
    if display_message:
        cv2.putText(frame, display_message, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
   
    cv2.waitKey(1)
