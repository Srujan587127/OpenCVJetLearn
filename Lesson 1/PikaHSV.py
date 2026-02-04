import cv2
image = cv2.imread("pikachuimage.jpg", cv2.IMREAD_COLOR)
if image is None:
    print("Image not found: Check the file path")
else:
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Orignal Pikachu Image", image)
    cv2.waitKey(0)
    cv2.imshow("Pikachu in HSV", hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()