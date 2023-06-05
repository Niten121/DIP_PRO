import cv2

img1 = cv2.imread("img1.png",1)
cv2.imshow('Image 1', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img2 = cv2.imread("img2.png", 1)
cv2.imshow('Image 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

sub_img = cv2.subtract(img1, img2)
cv2.imshow('Subtracted Image', sub_img)

add_img = cv2.add(img1, img2)
cv2.imshow('add', add_img)

div_img = cv2.divide(img1, img2)
cv2.imshow('div Image', div_img)

mul_img = cv2.multiply(img1, img2)
cv2.imshow('mul Image', mul_img)
cv2.waitKey(0)
cv2.destroyAllWindows()