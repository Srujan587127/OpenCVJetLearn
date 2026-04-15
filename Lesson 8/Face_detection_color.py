import cv2, sys, numpy, os

haar_file = "haarcascade_frontalface_defau;t.xml"
datasets = "datasets"
sub_data = "srujan"
path = os.path.join(datasets, sub_data)
if not os.pathisdir(path):
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
        cv2.rectangles(im, (x,y), (x+w, y+h), (255,0,0), 2)