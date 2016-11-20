'''
color_segment.py - given a color RGB image, convert to HSV color space
and play with controls to segment the image based on choice of color,
get the HSV bounds for that color
Author: Esha Uboweja (euboweja)
'''
# Import Libraries
import cv2
import numpy as np
import sys

hmax = 180
smax = 255
vmax = 255
# Callback function for trackbar
def nothing(x):
    pass
# Read image in color format
if len(sys.argv) > 1:
    im_name = sys.argv[1]
else:
    im_name = "../images/birds.jpg"
img_str = im_name.split("/")[-1]

birdsImg = cv2.imread(im_name)
# Convert to HSV space
birdsHSV = cv2.cvtColor(birdsImg, cv2.COLOR_BGR2HSV)
result = birdsImg

# Create a blank image, and a window
segmented = np.zeros(birdsImg.shape, np.uint8)
cv2.namedWindow("Segmented")
# Create trackbars for selecting [H,S,V] values
cv2.createTrackbar("H_low", "Segmented", 0, hmax, nothing)
cv2.createTrackbar("S_low", "Segmented", 0, smax, nothing)
cv2.createTrackbar("V_low", "Segmented", 0, vmax, nothing)
# Create trackbars for selecting [H,S,V] values
cv2.createTrackbar("H_high", "Segmented", 0, hmax, nothing)
cv2.createTrackbar("S_high", "Segmented", 0, smax, nothing)
cv2.createTrackbar("V_high", "Segmented", 0, vmax, nothing)

# Create switch for ON/OFF functionality
switch = "0 : OFF \t1 : ON"
cv2.createTrackbar(switch, "Segmented", 0, 1, nothing)

# Create switch for printing the HSV bounds
def print_hsv(x):
    if x == 1:
        H_low = cv2.getTrackbarPos("H_low", "Segmented")
        S_low = cv2.getTrackbarPos("S_low", "Segmented")
        V_low = cv2.getTrackbarPos("V_low", "Segmented")
        H_high = cv2.getTrackbarPos("H_high", "Segmented")
        S_high = cv2.getTrackbarPos("S_high", "Segmented")
        V_high = cv2.getTrackbarPos("V_high", "Segmented")

        low = np.array([H_low, S_low, V_low])
        high = np.array([H_high, S_high, V_high])
        print "HSV Low: ", low, ", High: ", high

        save_name = 'seg' + '_lh_' + str(low[0]) + '_ls_' + str(low[1]) + '_lv_' + str(low[2]) \
                    + '_hh_' + str(high[0]) + '_hs_' + str(high[1]) + '_hv_' + str(high[2]) \
                    + '_' + img_str

        mask = cv2.inRange(birdsHSV, low, high)
        result = cv2.bitwise_and(birdsImg, birdsImg, mask = mask)
        res_name = '../results/' + save_name
        print "Saving result as", res_name
        cv2.imwrite(res_name, result)

hsv_bound_print = "0 : OFF\t1: PRINT"
cv2.createTrackbar(hsv_bound_print, "Segmented", 0, 1, print_hsv)

# Wait for user input in GUI
while True:
    cv2.imshow("Segmented", result)
    key = cv2.waitKey(20)
    if key == 27:
        break
        
    # Get curruent trackbar positions => values
    H_low = cv2.getTrackbarPos("H_low", "Segmented")
    S_low = cv2.getTrackbarPos("S_low", "Segmented")
    V_low = cv2.getTrackbarPos("V_low", "Segmented")
    H_high = cv2.getTrackbarPos("H_high", "Segmented")
    S_high = cv2.getTrackbarPos("S_high", "Segmented")
    V_high = cv2.getTrackbarPos("V_high", "Segmented")
    s = cv2.getTrackbarPos(switch, "Segmented")
    do_print = cv2.getTrackbarPos(hsv_bound_print, "Segmented")
    
    low = np.array([H_low, S_low, V_low])
    high = np.array([H_high, S_high, V_high])
    
    if s:
        # Filter out components with values in selected range
        # Threshold HSV image
        mask = cv2.inRange(birdsHSV, low, high)
        result = cv2.bitwise_and(birdsImg, birdsImg, mask = mask)

# After key press, destroy all external windows
cv2.destroyAllWindows()

print "low: ", low, ", high: ", high