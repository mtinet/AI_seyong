import cv2

img = cv2.imread('images/test.jpg', cv2.IMREAD_COLOR)

cartoon_img = cv2.stylization(img, sigma_s=50, sigma_r=0.5)

cv2.imshow('original', img)
cv2.imshow('cartoon', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cartoon_test.jpg', cartoon_img)
