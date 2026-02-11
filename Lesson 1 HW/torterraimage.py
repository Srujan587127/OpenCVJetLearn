import cv2
import os

img_color = cv2.imread("TorterraImage.jpg", cv2.IMREAD_COLOR)

img_gray = cv2.imread("TorterraImage.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Torterra Color", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Torterra Black and White", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

save_directory = r"\\Users\\srujankallem\\Desktop\\Jetlearn\\Open CV\\LESSON 1 HW"
os.chdir(save_directory)

cv2.imwrite("TorterraBlackandWhite.jpg", img_gray)
print("Successfully Saved")
