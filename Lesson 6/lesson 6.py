import os
import cv2
from PIL import Image

mean_height = 0
mean_width = 0

image_files = []

for file in os.listdir("."): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        image_files.append(file)

number_of_images = len(image_files)
for file in image_files:
    img = Image.open(file)
    width,height = img.size
    mean_width += width
    mean_height += height

mean_width = mean_width//number_of_images
mean_height = mean_height//number_of_images
print("average width:", mean_width)
print("average height:", mean_height)

for file in image_files:
    img = Image.open(file)
    width,height = img.size
    print(width,height)
    imgresize = img.resize((mean_width, mean_height), Image.LANCZOS)
    imgresize.save(file, "jpeg", quality = 95)
    print(file,"is resized")

video_name = "myfirstvideo.avi"
frame = cv2.imread(image_files[0])
height,width,layers = frame.shape
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

for image in image_files:
    frame = cv2.imread(image)
    video.write(frame)
video.release()

cv2.destroyAllWindows()
print("video created succesfully")
cap = cv2.VideoCapture(video_name)

while True:
    ret, frame = cap.read()
    if not ret:
        break 
    cv2.imshow("video slideshow", frame)
    if cv2.waitKey(1000)& 0xFF == ord ("q"):
        break 
cap.release()
cv2.destroyAllWindows()