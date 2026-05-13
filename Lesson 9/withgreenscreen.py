import cv2
import numpy as np

cap = cv2.VideoCapture(0)
bg = cv2.imread("spacebackground.jpg")
bg = cv2.resize(bg, (640, 480))
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
    person = cv2.bitwise_and(frame, frame, mask = mask_inv)
    background = cv2.bitwise_and(bg, bg, mask = mask)
    final = cv2.add(person, background)
    cv2.imshow("Virtual Background", final)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows