import cv2
import numpy as np

# --- Load Image ---
img = cv2.imread("black.jpeg")

# Resize (optional)
img = cv2.resize(img, (512, 512))

# --- Step 1: Normalize histogram (stretch contrast globally) ---
norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# --- Step 2: Apply CLAHE (local adaptive enhancement) ---
lab = cv2.cvtColor(norm, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
cl = clahe.apply(l)
lab = cv2.merge((cl, a, b))
clahe_result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# --- Step 3: Gentle Gamma correction to bring up midtones ---
gamma = 0.5
gamma_corrected = np.power(clahe_result / 255.0, gamma)
gamma_corrected = np.uint8(gamma_corrected * 255)

# --- Step 4: Denoise ---
denoised = cv2.fastNlMeansDenoisingColored(gamma_corrected, None, 7, 7, 7, 21)

# --- Step 5: Deblur / Sharpen (Unsharp Mask) ---
blurred = cv2.GaussianBlur(denoised, (0, 0), 2)
sharp = cv2.addWeighted(denoised, 1.7, blurred, -0.7, 0)

# --- Step 6: Display Before vs After ---
combined = cv2.hconcat([img, sharp])
cv2.imshow("Before (Left)  |  After (Right)", combined)

# --- Step 7: Save result ---
cv2.imwrite("final_dark_restored.jpg", sharp)


cv2.waitKey(0)
cv2.destroyAllWindows()
