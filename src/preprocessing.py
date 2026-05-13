import cv2
import numpy as np


def preprocess_frame(frame):
    """Convert a BGR frame into a 3-channel image composed of grayscale, edges, and adaptive threshold."""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_frame, 100, 200)
    adaptive_thresh = cv2.adaptiveThreshold(
        gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    combined_frame = cv2.merge([gray_frame, edges, adaptive_thresh])
    return combined_frame
