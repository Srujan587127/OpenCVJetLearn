import cv2 
import os
img = cv2.imread("pikachuimage.jpg", cv2.IMREAD_COLOR) 
cv2.imshow("pikachu image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("pikachuimage.jpg", 0)
cv2.imshow("pikachu image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
save_directory = r"\\Users\\srujankallem\\Desktop\\Jetlearn\\Open CV\\LESSON 1"
img = cv2.imread("pikachuimage.jpg", 0)
cv2.imshow("Pikachu in Black and White", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.chdir(save_directory)
cv2.imwrite("PikachuBlackandWhite.jpg", img)
print("Successfully Saved")