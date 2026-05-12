from ultralytics import YOLO
import cv2
import random

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

model = YOLO("yolov8s.pt")

cv2.namedWindow("Real Time", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Real Time", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

class_colors = {}
class_names = model.names

while True:
    success, frame = cap.read()
    if not success:
        break

    object_count = 0

    results = model.predict(frame, stream=True, verbose=False, conf = 0.5)

    for r in results:
        boxes = r.boxes
        object_count += len(boxes)

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cls = int(box.cls[0])
            if cls not in class_colors:
                class_colors[cls] = [random.randint(0, 255) for _ in range(3)]
            color = class_colors[cls]

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

            conf = round(float(box.conf[0]), 2)
            label = model.names[cls]
            text =  f'{label} {conf:.2f}'

            cv2.putText(frame,text, (x1, max(35, y1 - 10)),cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.putText(frame, f'Total objects: {object_count}', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow("YOLOv8 - Rectangle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
