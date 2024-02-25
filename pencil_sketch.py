import cv2
#Read input image
img=cv2.imread("luffy.jpg")       
#Step-2
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert_gray=cv2.bitwise_not(gray)
#Step-3
blur=cv2.GaussianBlur(invert_gray,(49,49), 0,0)
invert_blur=cv2.bitwise_not(blur)
#Output sketch image
sketch=cv2.divide(gray,invert_blur,scale=255.0)
cv2.imwrite("luffy_sketch.jpg",sketch)