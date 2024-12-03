"""
Hand Tracing Module
By: Murtaza Hassan
Youtube: http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
Website: https://www.computervision.zone
"""
import cv2
import mediapipe as mp
import time

class HandTrackingModule:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        # Inisialisasi hands dengan mp.solutions.hands
        self.mpHands = mp.solutions.hands  # Inisialisasi mpHands disini
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils  # Menjaga drawing utils

    def findHands(self, img, draw=True):
        if img is None:  # Tambahkan pengecekan gambar kosong
            print("Error: Gambar kosong atau tidak dapat dibaca.")
            return img
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  # Memproses gambar

        if self.results.multi_hand_landmarks:  # Jika ada landmarks tangan
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # Menggambar landmarks

        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:  # Cek apakah ada landmarks tangan
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):  # Iterasi landmarks tangan
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])  # Simpan posisi landmark
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)  # Menandai posisi landmark
        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandTrackingModule(detectionCon=0.75, trackCon=0.75)  # Instance HandTrackingModule
    
    while True:
        success, img = cap.read()
        img = detector.findHands(img)  # Mencari tangan pada gambar
        lmList = detector.findPosition(img)  # Menemukan posisi landmarks
        
        if len(lmList) != 0:  # Jika landmarks ditemukan
            print(lmList[4])  # Menampilkan posisi landmark ke-4 (ibu jari)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)  # Menghitung FPS
        pTime = cTime


        cv2.waitKey(1)

if __name__ == "__main__":
    main()
