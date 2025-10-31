import cv2
import numpy as np

# --- Load Image ---
img = cv2.imread("butterfly.jpeg")

# Resize for consistency (optional)
img = cv2.resize(img, (512, 512))

# --- Step 1: Denoising using Non-Local Means ---
denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# --- Step 2: Deblurring / Sharpening using Unsharp Masking ---
blurred = cv2.GaussianBlur(denoised, (0, 0), 2)
final = cv2.addWeighted(denoised, 1.5, blurred, -0.5, 0)

# --- Step 3: Display Before and After ---
combined = cv2.hconcat([img, final])
cv2.imshow("Before (Left)  |  After (Right)", combined)

# --- Step 4: Save Final Output ---
cv2.imwrite("final_butterfly_clearvision.jpg", final)

cv2.waitKey(0)
cv2.destroyAllWindows()
