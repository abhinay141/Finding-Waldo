import cv2
import numpy as np
image = cv2.imread("waldobeach.jpg")
cv2.imshow('waldo beach',   image)
cv2.waitKey(0)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Waldo1.jpg",0)
result = cv2.matchTemplate(gray,    template,   cv2.TM_CCOEFF)
min_val,    max_val,    min_loc,    max_loc= cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + 100, top_left[1] + 100)
cv2.rectangle(image,top_left, bottom_right, (0,0,255), 5)
cv2.imshow('finding waldo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
