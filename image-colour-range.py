import cv2
import numpy as np

rawImage=cv2.imread('maple.JPG')
hsv=cv2.cvtColor(rawImage, cv2.COLOR_BGR2HSV)
# define range of red color in HSV
lower_red = np.array([0,100,50])
upper_red = np.array([10,255,255])

# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)
mask2 = 255-mask

grayImage=cv2.cvtColor(rawImage, cv2.COLOR_BGR2GRAY)
grayImage=cv2.cvtColor(grayImage, cv2.COLOR_GRAY2BGR)
colourPartImage = cv2.bitwise_and(rawImage,rawImage, mask= mask)
grayPartImage = cv2.bitwise_and(grayImage,grayImage, mask= mask2)
artImage=colourPartImage+grayPartImage
cv2.imshow('raw',rawImage)
cv2.imshow('mask',mask)
cv2.imshow('art',artImage)
cv2.waitKey(0)