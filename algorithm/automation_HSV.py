import cv2
import os
import numpy as np

# Path to the folder containing images
image_folder = "/home/wissal/git_image_processing/airport-image-processing/Airport"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

print(f"Found {len(image_files)} images.")

hsv_images = []  # List to store HSV images
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)
    if image is not None:
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv_images.append(hsv_image)
    else:
        print(f"Error loading image: {image_file}")

h_values, s_values, v_values = [], [], []

for hsv_image in hsv_images:
    h, s, v = cv2.split(hsv_image)  # Split into H, S, V channels
    h_values.extend(h.flatten())   # Flatten and collect all H values
    s_values.extend(s.flatten())   # Collect all S values
    v_values.extend(v.flatten())   # Collect all V values


import numpy as np

# Calculate percentiles for H, S, V to determine ranges
H_MIN = int(np.percentile(h_values, 5))  # Lower bound (5th percentile)
H_MAX = int(np.percentile(h_values, 95)) # Upper bound (95th percentile)

S_MIN = int(np.percentile(s_values, 5))
S_MAX = int(np.percentile(s_values, 95))

V_MIN = int(np.percentile(v_values, 5))
V_MAX = int(np.percentile(v_values, 95))

print(f"Hue Range: {H_MIN} - {H_MAX}")
print(f"Saturation Range: {S_MIN} - {S_MAX}")
print(f"Value Range: {V_MIN} - {V_MAX}")

lower_hue = np.array([H_MIN, S_MIN, V_MIN])
upper_hue = np.array([H_MAX, S_MAX, V_MAX])

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create a mask based on the HSV range
    mask = cv2.inRange(hsv_image, lower_hue, upper_hue)
    
    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Save or display the result
    result_path = os.path.join("Processed", image_file)
    os.makedirs("Processed", exist_ok=True)
    cv2.imwrite(result_path, result)

import matplotlib.pyplot as plt

plt.hist(h_values, bins=180, range=(0, 180), color='r', alpha=0.6, label='Hue')
plt.hist(s_values, bins=256, range=(0, 256), color='g', alpha=0.6, label='Saturation')
plt.hist(v_values, bins=256, range=(0, 256), color='b', alpha=0.6, label='Value')
plt.legend()
plt.title("HSV Pixel Distribution")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
