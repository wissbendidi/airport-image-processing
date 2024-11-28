import cv2
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def nothing(x):
    pass

# Load an image
image_path = "/home/wissal/git_image_processing/airport-image-processing/Airport/001.jpg"
image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window
cv2.namedWindow("Trackbars")

# Create trackbars for HSV range
cv2.createTrackbar("H_MIN", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("H_MAX", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("S_MIN", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S_MAX", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V_MIN", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V_MAX", "Trackbars", 255, 255, nothing)

while True:
    # Get current positions of trackbars
    h_min = cv2.getTrackbarPos("H_MIN", "Trackbars")
    h_max = cv2.getTrackbarPos("H_MAX", "Trackbars")
    s_min = cv2.getTrackbarPos("S_MIN", "Trackbars")
    s_max = cv2.getTrackbarPos("S_MAX", "Trackbars")
    v_min = cv2.getTrackbarPos("V_MIN", "Trackbars")
    v_max = cv2.getTrackbarPos("V_MAX", "Trackbars")

    # Define HSV range
    lower_hue = np.array([h_min, s_min, v_min])
    upper_hue = np.array([h_max, s_max, v_max])

    # Create a mask
    mask = cv2.inRange(hsv_image, lower_hue, upper_hue)

    # Apply the mask on the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Show the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered Image", result)

    # Break the loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
