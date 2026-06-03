import cv2
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

img = cv2.imread("./111.webp")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(img_gray,1.3,10,minSize=(100,100))
for (x,y,w,h) in faces:
    print(x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()