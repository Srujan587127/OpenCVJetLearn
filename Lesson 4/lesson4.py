import cv2
image = cv2.imread("pikachuimage.jpg")

start_point = (0,0)
end_point = (250,250)
color = (0,255,0)
thickness = 9

image = cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows


import cv2
image = cv2.imread("Pikachuimage.jpg")
start_point = (5,5)
end_point = (220,220)
color = (255,0,0)
thickness = 2

image = cv2.rectangle(image, start_point, end_point, color, thickness)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()