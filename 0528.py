import numpy as np
import cv2
import random
img = np.zeros((300,300,3), dtype=np.uint8)

print(img[0][0])
# img[0:300,0:100] = [128,140,0]
# img[0:300,-100:] = [128,140,0]

# img[200][299] = [0,0,255]
# img[0:,0:] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
for i in range(0,300):
    for j in range(0,300):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()