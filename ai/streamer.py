import cv2
from config import STREAM_URL


class ESP32Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(STREAM_URL)

    def open(self):
        return self.cap.isOpened()

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()