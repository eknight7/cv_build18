'''
gaussian_filter.py - given a color RGB image, try different
Gaussian kernels for image blurring
Author: Esha Uboweja (euboweja)
'''
# Import Libraries
import cv2
import numpy as np
import sys

# Callback function for trackbar
def nothing(x):
    pass

# Read image in color format
if len(sys.argv) > 1:
    im_name = sys.argv[1]
else:
    im_name = "../images/birds.jpg"

img = cv2.imread(im_name)
result = img

kernel_max = 20
# Create a blank image, and a window
segmented = np.zeros(img.shape, np.uint8)
cv2.namedWindow("Gaussian Blurred")
# Create trackbars for selecting [H,S,V] values
cv2.createTrackbar("kernel_rows", "Gaussian Blurred", 1, kernel_max, nothing)
cv2.createTrackbar("kernel_cols", "Gaussian Blurred", 1, kernel_max, nothing)

# Create switch for ON/OFF functionality
switch = "0 : OFF \n1 : ON"
cv2.createTrackbar(switch, "Gaussian Blurred", 0, 1, nothing)

# Wait for user input in GUI
while True:
    cv2.imshow("Gaussian Blurred", result)
    key = cv2.waitKey(20)
    if key == 27:
        break
        
    # Get curruent trackbar positions => values
    krow = cv2.getTrackbarPos("kernel_rows", "Gaussian Blurred")
    if krow % 2 == 0:
        krow += 1
    kcol = cv2.getTrackbarPos("kernel_cols", "Gaussian Blurred")
    if kcol % 2 == 0:
        kcol += 1
    s = cv2.getTrackbarPos(switch, "Gaussian Blurred")
    
    
    if s:
        # Apply Gaussian Blur to the image
        result = cv2.GaussianBlur(img, (krow, kcol), 0)
        
# After key press, destroy all external windows
cv2.destroyAllWindows()