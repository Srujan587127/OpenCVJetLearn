#Arithimatic Operations

import cv2
import numpy as np

image1 = cv2.imread("charizardimage.jpg")
image2 = cv2.imread("pikachuimage.jpg")

ImageSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow("Weighted Image", ImageSum)

cv2.waitKey(0)
cv2.destroyAllWindows()