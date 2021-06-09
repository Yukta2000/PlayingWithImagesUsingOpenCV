import cv2

back=cv2.imread("background.jpg")
jerry=cv2.imread("jerry.jpg")
mickey=cv2.imread("mickey mouse.jpg")
nat=cv2.imread("nature.jpg")
pooh=cv2.imread("winnie.png")

jerry=jerry[1:255,20:180]
mickey=mickey[1:255,40:210]

back[1:194,40:210]= mickey
back[1:169,260:560]=nat
back[1:253,600:760]=jerry
back[200:410,290:530]=pooh
cv2.imshow("Collage",back)
cv2.waitKey()
cv2.destroyAllWindows()
