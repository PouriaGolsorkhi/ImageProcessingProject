from retinaface import RetinaFace
import cv2

def faceDetector(images, path):
    output = []
    for i in range(0,len(images)):
        tempImg = cv2.imread(f"{path}{images[i]}")
        if tempImg is not None:
            tempImg = cv2.cvtColor(tempImg, cv2.COLOR_BGR2RGB)
            output.append(RetinaFace.detect_faces(tempImg))
    return output