import cv2 
img = cv2.imread("pikachuimage.jpg", cv2.IMREAD_COLOR) 
cv2.imshow("pikachu image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = cv2.imread("pikachuimage.jpg", 0)
cv2.imshow("pikachu image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()