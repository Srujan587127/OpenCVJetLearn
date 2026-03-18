import cv2
import numpy as np

img = cv2.imread("coins.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (9,9), 2)

circles = cv2.HoughCircles(gray, 
                           cv2.HOUGH_GRADIENT, 
                           dp = 1.2, 
                           minDist = 80,
                           param1 = 100,
                           param2 = 40,
                           minRadius = 30,
                           maxRadius = 120)



if circles is not None:
    
    circles = np.uint16(np.around(circles))
    
    for i in circles[0, :]:
        
       
        cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
        
        
        cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)


cv2.imshow("Coins Detected", img)

cv2.waitKey(0)

cv2.destroyAllWindows()