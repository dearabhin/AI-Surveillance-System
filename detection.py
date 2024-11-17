import cv2
from ultralytics import YOLO

model = YOLO("models/pre-trained/yolov8n.pt")

def detect_people(frame):
    results = model(frame)
    return results[0]
