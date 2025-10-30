import cv2

# ---------- Load Image ----------
img = cv2.imread("monkey.jpeg")

# ---------- 1. Gaussian Blur ----------
gaussian = cv2.GaussianBlur(img, (5,5), 1.0)
cv2.imwrite("gaussian_denoised.jpg", gaussian)

# ---------- 2. Median Filter ----------
median = cv2.medianBlur(img, 5)
cv2.imwrite("median_denoised.jpg", median)

# ---------- 3. Bilateral Filter ----------
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imwrite("bilateral_denoised.jpg", bilateral)

# ---------- 4. Non-Local Means Denoising ----------
nlm = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
cv2.imwrite("nlm_denoised.jpg", nlm)

# ---------- Display Results ----------
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Filter", median)
cv2.imshow("Bilateral Filter", bilateral)
cv2.imshow("Non-Local Means", nlm)

print("Denoising completed — results saved as:")
print("gaussian_denoised.jpg, median_denoised.jpg, bilateral_denoised.jpg, nlm_denoised.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
