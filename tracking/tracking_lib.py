import cv2
import numpy as np

def capture_frame():
	# Open the "default" camera
	vc = cv2.VideoCapture(0)
	# Check if we succeeded in opening camera feed
	if vc.isOpened():
	    rval, frame = vc.read()
	else:
	    rval = False
	# Display captured frames in a new window
	cv2.namedWindow("Camera Video Feed")

	while rval:
	    cv2.imshow("Camera Video Feed", frame)
	    # cv2.imshow("Camera Video Feed", result)
	    rval, frame = vc.read()
	    key = cv2.waitKey(20)
	    if key == 27: # User pressed ESC key
	        break
	    elif key == ord('s'):
	        break
	# Destroy window
	cv2.destroyWindow("Camera Video Feed")
	# Close VideoCapture feed -- Important!
	vc.release()

	# Save the frame
	cv2.imwrite('../images/captured_frame.png', frame)
	return frame

def track_obj(low_hsv, high_hsv):
	# Open the "default" camera
	vc = cv2.VideoCapture(0)
	# Check if we succeeded in opening camera feed
	if vc.isOpened():
	    rval, frame = vc.read()
	else:
	    rval = False
	# Display captured frames in a new window
	cv2.namedWindow("Camera Video Feed")
	# Display filtered object frame in a new window
	cv2.namedWindow("Tracking")

	result = frame

	while rval:
	    cv2.imshow("Camera Video Feed", frame)
	    cv2.imshow("Tracking", result)
	    rval, frame = vc.read()
	    # Convert to HSV space
	    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	    # Filter out components with values in selected range
	    # Threshold HSV image
	    mask = cv2.inRange(frameHSV, low_hsv, high_hsv)
	    result = cv2.bitwise_and(frame, frame, mask = mask)
	    # Wait for ESC key press
	    key = cv2.waitKey(20)
	    if key == 27: # User pressed ESC key
	        break
	# Destroy window
	cv2.destroyWindow("Camera Video Feed")
	# Close VideoCapture feed -- Important!
	vc.release()

def capture_obj_color(frame):
	print "Please select object color to track object."

	hmax = 180
	smax = 255
	vmax = 255
	# Callback function for trackbar
	def nothing(x):
	    pass

	# Convert to HSV space
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	result = frame

	# Create a blank image, and a window
	segmented = np.zeros(frameHSV.shape, np.uint8)
	window_name = "Select object color"
	cv2.namedWindow(window_name)
	# Create trackbars for selecting [H,S,V] values
	cv2.createTrackbar("H_low", window_name, 0, hmax, nothing)
	cv2.createTrackbar("S_low", window_name, 0, smax, nothing)
	cv2.createTrackbar("V_low", window_name, 0, vmax, nothing)
	# Create trackbars for selecting [H,S,V] values
	cv2.createTrackbar("H_high", window_name, 0, hmax, nothing)
	cv2.createTrackbar("S_high", window_name, 0, smax, nothing)
	cv2.createTrackbar("V_high", window_name, 0, vmax, nothing)

	# Create switch for ON/OFF functionality
	switch = "0 : OFF \t1 : ON"
	cv2.createTrackbar(switch, window_name, 0, 1, nothing)

	# Callback function for printing trackbar
	def print_hsv(x):
	    if x == 1:
	        H_low = cv2.getTrackbarPos("H_low", window_name)
	        S_low = cv2.getTrackbarPos("S_low", window_name)
	        V_low = cv2.getTrackbarPos("V_low", window_name)
	        H_high = cv2.getTrackbarPos("H_high", window_name)
	        S_high = cv2.getTrackbarPos("S_high", window_name)
	        V_high = cv2.getTrackbarPos("V_high", window_name)

	        low = np.array([H_low, S_low, V_low])
	        high = np.array([H_high, S_high, V_high])
	        print "HSV Low: ", low, ", High: ", high

	        save_name = 'seg' + '_lh_' + str(low[0]) + '_ls_' + str(low[1]) + '_lv_' + str(low[2]) \
	                    + '_hh_' + str(high[0]) + '_hs_' + str(high[1]) + '_hv_' + str(high[2]) \
	                    + '_frame.png'

	        mask = cv2.inRange(frameHSV, low, high)
	        result = cv2.bitwise_and(frame, frame, mask = mask)
	        res_name = '../results/' + save_name
	        print "Saving result as", res_name
	        cv2.imwrite(res_name, result)

	# Create switch for printing the HSV bounds
	hsv_bound_print = "0 : OFF\t1: PRINT"
	cv2.createTrackbar(hsv_bound_print, window_name, 0, 1, print_hsv)

	# Wait for user input in GUI
	while True:
	    cv2.imshow(window_name, result)
	    key = cv2.waitKey(20)
	    if key == 27:
	        break
	        
	    # Get curruent trackbar positions => values
	    H_low = cv2.getTrackbarPos("H_low", window_name)
	    S_low = cv2.getTrackbarPos("S_low", window_name)
	    V_low = cv2.getTrackbarPos("V_low", window_name)
	    H_high = cv2.getTrackbarPos("H_high", window_name)
	    S_high = cv2.getTrackbarPos("S_high", window_name)
	    V_high = cv2.getTrackbarPos("V_high", window_name)
	    s = cv2.getTrackbarPos(switch, window_name)
	    do_print = cv2.getTrackbarPos(hsv_bound_print, window_name)
	    
	    low = np.array([H_low, S_low, V_low])
	    high = np.array([H_high, S_high, V_high])
	    
	    if s:
	        # Filter out components with values in selected range
	        # Threshold HSV image
	        mask = cv2.inRange(frameHSV, low, high)
	        result = cv2.bitwise_and(frame, frame, mask = mask)

	# After key press, destroy all external windows
	cv2.destroyAllWindows()

	print "low: ", low, ", high: ", high
	return (low, high)
