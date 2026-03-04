import cv2
import numpy as np

img = cv2.imread("pikachuimage.jpg", 1)

kernel1 = np.ones((3,3), np.uint8)
kernel2 = np.ones((5,5), np.uint8)
kernel3 = np.ones((7,7), np.uint8)


erosion1 = cv2.erode(img, kernel1)
erosion2 = cv2.erode(img, kernel2)
erosion3 = cv2.erode(img, kernel3)


cv2.imshow("Original Image", img)
cv2.imshow("Erosion 3x3", erosion1)
cv2.imshow("Erosion 5x5", erosion2)
cv2.imshow("Erosion 7x7", erosion3)

cv2.waitKey(0)
cv2.destroyAllWindows()