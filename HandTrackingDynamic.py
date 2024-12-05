import cv2
import mediapipe as mp
import pyautogui
import time
import math

class HandTrackingDynamic:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.__mode__ = mode
        self.__maxHands__ = maxHands
        self.__detectionCon__ = detectionCon
        self.__trackCon__ = trackCon
        self.handsMp = mp.solutions.hands
        self.hands = self.handsMp.Hands(min_detection_confidence=detectionCon, min_tracking_confidence=trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]  # Finger tips

    def findFingers(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  
        if self.results.multi_hand_landmarks: 
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms, self.handsMp.HAND_CONNECTIONS)
        return frame

    def findPosition(self, frame, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmsList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmsList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
            if draw:
                cv2.rectangle(frame, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

        return self.lmsList, bbox

    def findDistance(self, id1, id2, frame):
    # Ensure that the landmarks are available before trying to calculate the distance
        if len(self.lmsList) > 0:
            # Get the (x, y) positions of the two landmarks
            x1, y1 = self.lmsList[id1][1], self.lmsList[id1][2]
            x2, y2 = self.lmsList[id2][1], self.lmsList[id2][2]
            
            # Calculate the Euclidean distance between the two points
            length = math.hypot(x2 - x1, y2 - y1)
            
            # Optionally, draw a line between the two points
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
            # Prepare lineInfo containing the coordinates of the points
            lineInfo = ((x1, y1), (x2, y2))
            
            # Return the distance, frame with the line, and lineInfo
            return length, frame, lineInfo
        return None, frame, None


def main():
    ctime = 0
    ptime = 0
    cap = cv2.VideoCapture(0)
    detector = HandTrackingDynamic()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()
        frame = detector.findFingers(frame)
        lmsList, bbox = detector.findPosition(frame)

        # Check if we have landmarks
        if len(lmsList) != 0:
            ctime = time.time()
            fps = 1 / (ctime - ptime)
            ptime = ctime

            # Example: calculate the distance between the tip of the index finger (id 8) and the tip of the middle finger (id 12)
            length, frame = detector.findDistance(8, 12, frame)
            if length:
                cv2.putText(frame, f"Dist: {int(length)}", (50, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
