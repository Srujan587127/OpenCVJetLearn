import cv2
import mediapipe as mp
import numpy as np
import sys

cap = cv2.VideoCapture(0)

bg = cv2.imread("spacebackground.jpg")
bg = cv2.resize(bg, (640, 480))

mp_selfie = mp.solutions.selfie_segmentation
segment = mp_selfie.SelfieSegmentation(model_selection=1)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = segment.process(rgb)

    mask = result.segmentation_mask > 0.5

    output = np.where(mask[:, :, None], frame, bg)

    
    cv2.putText(
        output,
        "Hello",
        (120, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("Virtual Background", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()