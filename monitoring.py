import cv2
from detection import detect_people
from alert_system import send_alert

DANGER_ZONE_Y = 400  # Example pixel value for danger zone limit

def monitor_beach(video_source=0):
    cap = cv2.VideoCapture(video_source)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = detect_people(frame)

        for box in results.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            if y2 > DANGER_ZONE_Y:  # Check if crossing danger zone
                cv2.putText(frame, "DANGER!", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                send_alert()

        cv2.imshow("Beach Surveillance", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
