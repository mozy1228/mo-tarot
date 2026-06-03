import cv2
img = cv2.imread("./cat.jpg", cv2.IMREAD_REDUCED_COLOR_2)

# img2 = cv2.rotate(img,cv2.ROTATE_180)
# img_flip = cv2.flip(img,1)
cv2.line(img,(0,0),(100,100),(0,0,225),5)
cv2.rectangle(img,(100,100),(300,300),(255,0,225),5)
cv2.circle(img,(100,100),10,(0,0,255),-1)
cv2.imshow("cat",img)
cv2.waitKey(0)
cv2.destroyAllWindows()