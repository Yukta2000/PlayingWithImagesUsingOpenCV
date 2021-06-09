import cv2
photo1=cv2.imread("jerry.jpg")
photo2=cv2.imread("mickey mouse.jpg")
jerryFace=photo1[1:100,60:180]
mickeyFace=photo2[1:90,60:180]
new1=cv2.imread("jerry.jpg")
new2=cv2.imread("mickey mouse.jpg")
new1[1:90,60:180]=mickeyFace
new2[1:100,60:180]=jerryFace
cv2.imshow("Jerry Mickey face",new1)
cv2.imshow("Mickey Jerry face",new2)

cv2.imshow("Jerry Original",photo1)
cv2.imshow("Mickey Original",photo2)
cv2.imshow("Jerry face",jerryFace)
cv2.imshow("Mickey face",mickeyFace)
cv2.waitKey()
cv2.destroyAllWindows()
