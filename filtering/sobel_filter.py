'''
sobel_filter.py - given a color RGB image, try different
Sobel filters for edge detection
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

img = cv2.imread(im_name, 0)
img_str = im_name.split("/")[-1]

# Apply Gaussian Blur to the image
blurred = cv2.GaussianBlur(img, (3, 3), 0)
# Convolute with sobel filter
# X direction
sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=11) 
# Y direction
sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=11)

# Display image in new window
cv2.imshow("Sobel X", sobelx)
res_name = '../results/' + 'sobel_x_' + img_str
cv2.imwrite(res_name, sobelx)

# Display image in new window
cv2.imshow("Sobel Y", sobely)
res_name = '../results/' + 'sobel_y_' + img_str
cv2.imwrite(res_name, sobely)

# Wait for key press on external window
cv2.waitKey(0)

# After key press, destroy all external windows
cv2.destroyAllWindows()