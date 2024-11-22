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
    # Read the image in grayscale
    picture = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if picture is None:
        print(f"Error: Image not found at {image_path}")
        return

    # Define angles and initialize min_pixel_image
    angles = np.arange(-90, 91, 1)
    min_pixel_image = np.full(picture.shape, 255, dtype=np.uint8)

    # Perform morphological operations
    for angle in angles:
        struct_element = strel.build('line', 35, angle)
        image_closed = first_functions.myclose(picture, struct_element)
        min_pixel_image = np.minimum(min_pixel_image, image_closed)

    # Thresholding
    image_bin = seuil(min_pixel_image, 32)

    # Display intermediate result
    cv2.imshow("Binary Image", image_bin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Open and close operations
    image_bin1 = first_functions.myopen(image_bin, strel.build('square', 2))
    image_bin2 = first_functions.myclose(image_bin1, strel.build('square', 2))

    # Gradient for contours
    contours = first_functions.mygradient(image_bin2, strel.build("square", 1))

    # Draw contours in red on the original image
    picture = cv2.imread(image_path)
    picture[contours > 0] = [0, 0, 255]

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
    image_path = os.path.join(script_dir, "../images", image_filename)

    # Process the image
    process_image(image_path)

if __name__ == "__main__":
    main()
