import os
import cv2
from PIL import Image

path = r"\Users\srujankallem\Desktop\Jetlearn\Open CV\Lesson 6"
os.chdir(path)

mean_height = 0
mean_width = 0

image_files = []

for file in os.listdir(","): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        image_files.append(file)

number_of_images = len(image_files)
for file in image_files:
    img = Image.open(os.path.join(path,file))
    width,height = img.size
    mean_width += width
    mean_height += height

mean_width = mean_width//number_of_images
mean_height = mean_height//number_of_images
print("average width:", mean_width)
print("average height:", mean_height)

for file in image_files:
    img = Image.open(os.path.join(path,file))
    width,height = img.size
    print(width,height)
    imgresize = img.resize((mean_width, mean_height), Image.LANCZOS)
    imgresize.save(file, "jpeg", quality = 95)
    print(file,"is resized")

video_name = "myfirstvideo.avi"
frame = cv2.imread(image_files[0])
height,width,layers = frame.shape
fourcc = cv2.VideoWriter_fourcc(*"XVID")