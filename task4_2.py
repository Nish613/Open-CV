import cv2
import numpy as np

# --- Load Image ---
img = cv2.imread("monkey.jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found.")
    exit()

img = cv2.resize(img, (512, 512))

# --- Step 1: Estimate Blur and Apply Unsharp Masking ---
blurred = cv2.GaussianBlur(img, (0, 0), 3)
unsharp = cv2.addWeighted(img, 1.7, blurred, -0.7, 0)

# --- Step 2: High-pass filter for fine detail recovery ---
# Create a Laplacian kernel
laplacian = cv2.Laplacian(unsharp, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# Combine Laplacian edges with the unsharp result
final = cv2.addWeighted(unsharp, 1.2, laplacian, 0.3, 0)

# --- Step 3: Display Results ---
combined = cv2.hconcat([img, final])
cv2.imshow("Before (Left)  |  After (Right)", combined)

# --- Step 4: Save the Final Output ---
cv2.imwrite("final_monkey_deblurred.jpg", final)
print("✅ Final sharpened and deblurred image saved as 'final_monkey_deblurred.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()
