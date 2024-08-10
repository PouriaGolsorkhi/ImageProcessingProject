import cv2
import matplotlib.pyplot as plt
import numpy as np

def manualConvolution_3x3(mat1, mat2):
    outputmat = [[1 for y in mat1[0]] for x in mat1]
    for i in range(0,len(mat1)):
        for j in range(0,len(mat1[i])):
            outputmat[i][j] = mat1[i][j]*mat2[i][j]
    
    return outputmat
            

def applyConvOnImage(img, customKernel):
    
    if len(img.shape) ==3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    img_height , img_width = img.shape
    outputImg = np.zeros_like(img)
    
    for i in range(1, img_width):
        for j in range(1, img_height):
            tempMat = img[i-1:i+2 , j-1:j+2]
            convRes = manualConvolution_3x3(tempMat.tolist(), customKernel)
            outputImg[i,j] = np.sum(convRes) 
            
    
    return outputImg
            
            