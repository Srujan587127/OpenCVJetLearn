#Arithimatic Operations

import cv2
import numpy as np

image1 = cv2.imread("charizardimage.jpg")
image2 = cv2.imread("pikachuimage.jpg")

image2 = cv2.resize(image2,(image1.shape[1], image1.shape[0]))

ImageSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow("Weighted Image", ImageSum) 
Imagesub = cv2.subtract(image1, image2)
cv2.imshow("subtracted image", Imagesub)

cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("pikachuimage.jpg", 1)
cv2.imshow("original image", img)

resized = cv2.resize(img,(500,250))
cv2.imshow("reduced image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pikachuimage.jpg", 1)
kernel = np.ones((5,5), np.uint8)
eroded_image = cv2.erode(image, kernel)
cv2.imshow("eroded image", eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pikachuimage.jpg")
gaussian = cv2.GaussianBlur(image,(7,7), 0)
cv2.imshow("Gassiun Blur", gaussian)
cv2.waitKey(0)
median = cv2.medianBlur(image, 5)
cv2.imshow("median blur", median)
cv2.waitKey(0)
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("bilateral blur", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pikachuimage.jpg")
borderimage = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)
cv2.imshow("border image", borderimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pikachuimage.jpg")
borderimage = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("border image", borderimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
