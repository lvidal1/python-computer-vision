import numpy as np
import cv2

original_image = cv2.imread('bird.jpg', cv2.IMREAD_COLOR)

# we have to transform the image into grayscale
# OPENCV handles BGR instead of RGB
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Laplacian Kernel
kernel = np.array([[0,1,0],[1,-4,1], [0,1,0]])

edge_image = cv2.filter2D(gray_image, -1, kernel)

edge_image_laplacian = cv2.Laplacian(gray_image, -1)

cv2.imshow('Original Image', gray_image)
cv2.imshow('Edge Image', edge_image)
cv2.imshow('Edge Image (Laplacian)', edge_image_laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
