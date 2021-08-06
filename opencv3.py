# import  cv2
# img=cv2.imread('1.jpg')

# cv2.waitKey(0)

# # gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray img",gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# method 2
import cv2
img=cv2.imread('1.jpg',0)
cv2.imshow('im',img)
cv2.waitKey(0)
cv2.destroyAllWindows()