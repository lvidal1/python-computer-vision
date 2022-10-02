import numpy as np
import cv2

original_image = cv2.imread('bird.jpg', cv2.IMREAD_COLOR)

FILTER_ROWS = 5
FILTER_COLUMNS = 5
NORMALIZATION = FILTER_ROWS * FILTER_COLUMNS

kernel = np.ones((FILTER_ROWS,FILTER_COLUMNS)) / NORMALIZATION

# -1 "destination depth"
blur_image = cv2.filter2D(original_image, -1, kernel)

# gaussian blur is used to reduce noise

cv2.imshow('Original Image', original_image)
cv2.imshow('Blurred Image', blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
print(kernel)