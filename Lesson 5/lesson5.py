import cv2
import numpy as np

img = cv2.imread("eyes.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (9,9), 2)

detected_circles = cv2.HoughCircles(
    gray_blur, 
    cv2.HOUGH_GRADIENT,
    dp = 1.2, 
    minDist = 100,
    param1 = 100,
    param2 = 40,
    minRadius = 30,
    maxRadius = 80
)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a,b,r = pt[0], pt[1], pt[2]

        cv2.circle(img, (a,b), r, (0,255,0), 3)
        cv2.circle(img, (a,b), 2, (0,0,255), 3)

cv2.imshow("Detected Pupils: ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

image = cv2.imread("circles.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
    exit()

_, thresh = cv2.threshold(image, 120,255,cv2.THRESH_BINARY_INV)

thresh = cv2.GuassianBlur(thresh, (5,5), 0)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200

params.filterByColor = True
params.blobColor = 255

params.filterByArea = True
params.minArea = 1000
params.maxArea = 50000

params.filterByCircularity = True
params.minCircularity = 0.7

params.filterByConvexity = False

params.filterByInertia = False