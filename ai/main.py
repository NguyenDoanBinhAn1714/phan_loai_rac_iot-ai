import cv2
import time
from streamer import ESP32Camera
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

camera = ESP32Camera()

if not camera.open():
    print("❌ Không kết nối được ESP32-CAM")
    exit()

print("✅ Đã kết nối ESP32-CAM")

frame_count = 0

while True:

    ret, frame = camera.read()

    if not ret:
        print("⚠️ Mất frame, reconnect...")
        camera.release()
        camera.open()
        continue

    frame = cv2.resize(frame, (320, 240))

    frame_count += 1

    if frame_count % 3 == 0:
        results = model(frame, imgsz=320, conf=0.4)
        frame = results[0].plot()

    cv2.imshow("ESP32-CAM + YOLO", frame)

    time.sleep(0.03)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()