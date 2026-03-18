import os 
import cv2
from tkinter import *
from PIL import Image, ImageTk

image_files = []

for file in os.listdir(","): 
    if file.endswith(".jpg") or file.endswith("png") or file.endswith(".jpeg"):
        image_files.append(file)

current_image = 0

root = Tk()
root.title("Photo Gallery with OpenCV")

def load_image():
    global Photo
    image_path = os.path.join(image_files[current_image])
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RBG)
    img = Image.fromarray(img)
    img = img.resize((500,400))
    photo = ImageTk.PhotoImage(img)
    label.config(image = photo)
    label.image = photo

def next_image():
    global current_image
    current_image += 1
    if current_image >= len(image_files):
        current_image = 0
    load_image()

def prev_image():
    global current_image
    current_image -= 1
    if current_image < 0:
        current_image = len(image_files)
    load_image()

def grayscale():
    global Photo
    image_path = os.path.join(image_files[current_image])
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.Color_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.Color_GRAY2RGB)
    img = Image.fromarray(gray)
    img = img.resize((500, 400))
    photo = ImageTk.PhtoImage(img)
    label.config(image = photo)
    label.image = photo

label = Label(root)
label.pack()
prev_btn = Button(root, text = "Previous", command=prev_image)
prev_btn.pack(side = LEFT, padx = 10, pady = 10)

next_btn = Button(root, text = "Next", command = next_image)
next_btn.pack(side = LEFT, padx = 10, pady = 10)

gray_btn = Button(root, text = "Grayscale Filter", command=grayscale)
gray_btn.pack(side = RIGHT, padx = 10, pady = 10)

root.mainloop