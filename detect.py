from mtcnn.mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt
import os

img = cv2.imread("img11.jpg")
temp = img.copy()
detector = MTCNN()
out = detector.detect_faces(img)
d = 1
#print(detector.detect_faces(img))
for i in out:
    for[x, y, w, h] in [i['box']]:
        print(x,y,w,h)
        cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0),10)
        sub_face = temp[y:y+h,x:x+w]
        plt.imshow(cv2.cvtColor(sub_face, cv2.COLOR_BGR2RGB))
        plt.show()
        directory = "face"+str(d)
        if not os.path.exists(directory):
            os.makedirs(directory)
            cv2.imwrite("./face"+str(d)+"/"+"face"+str(d)+".jpg",sub_face)
        d+=1
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
cv2.imwrite("img.jpg",img)