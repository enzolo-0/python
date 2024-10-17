import cv2 as cv
img = cv.imread("assets/bird.jpeg")
cv.imshow("BIRD Window", img)
k = cv.waitKey(0)

cv.destroyAllWindows()
