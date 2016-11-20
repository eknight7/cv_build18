'''
color_track.py - given a live color video feed, select an object
to track based on color, then track that object in the feed
Author: Esha Uboweja (euboweja)
'''
# Import Libraries
import cv2
import numpy as np
import sys
from tracking_lib import *

# Capture a frame with the object
frame = capture_frame()

# Segment out object based on color
(low_hsv, high_hsv) = capture_obj_color(frame)

# Track object in live video feed
track_obj(low_hsv, high_hsv)
