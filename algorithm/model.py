author = "wissal bendidi"
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import numpy as np
from functions.myutil import myseuil_interactif, seuil
from functions import strel
from functions import first_functions


def process_image(image_path):
    # Read the image in color
    picture = cv2.imread(image_path)
    if picture is None:
        print(f"Error: Image not found at {image_path}")
        return

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(picture, cv2.COLOR_BGR2HSV)

    # Define HSV color range for detection (adjust these values based on your image)
    lower_hue = np.array([H_MIN, S_MIN, V_MIN])  # Set your lower bounds
    upper_hue = np.array([H_MAX, S_MAX, V_MAX])  # Set your upper bounds

    # Create a mask for the defined color range
    mask = cv2.inRange(hsv_image, lower_hue, upper_hue)

    # Perform morphological operations to clean the mask
    kernel = np.ones((5, 5), np.uint8)  # You can adjust the size based on your needs
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours from the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours in red on the original image
    for contour in contours:
        cv2.drawContours(picture, [contour], -1, (0, 0, 255), 2)  # Red color in BGR

    # Display final result
    cv2.imshow("Contours", picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Ensure an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python algorithm.py <image_filename>")
        return

    # Get the image filename from the command-line arguments
    image_filename = sys.argv[1]

    # Build the full path to the image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "../Airport", image_filename)

    # Process the image
    process_image(image_path)

if __name__ == "__main__":
    main()
