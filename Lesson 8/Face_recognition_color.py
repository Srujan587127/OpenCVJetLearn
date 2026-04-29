import cv2, sys, numpy, os

haar_file = "haarcascade_frontalface_default.xml"
datasets = "datasets"
sub_data = "srujan"
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.makedirs(path)

(width, height)= (130,100)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
count = 1

while count < 30:
    ret, im = webcam.read()
    if not ret:
        continue

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(im, (x,y), (x+w, y+h), (255,0,0), 2)

        face = im[y:y +h, x:x+w]
        face_resize = cv2.resize(face, (width, height))

        cv2.imwrite("%s/%s.png" % (path, count), face_resize)
        count += 1

    # display count in top-right corner
    text = f"Captured: {count-1} / 30"
    (h, w) = im.shape[:2]
    cv2.putText(im, text, (w - 220, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow("OpenCv = Face Capture", im)

    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()