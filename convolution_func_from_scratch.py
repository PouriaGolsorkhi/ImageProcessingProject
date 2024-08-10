import cv2
import matplotlib.pyplot as plt
import numpy as np

def manualConvolution_3x3(mat1, mat2):
    outputmat = np.zeros_like(mat1)
    height , width = mat1.shape
    for i in range(0,width):
        for j in range(0,height):
            outputmat[i,j] = mat1[i,j]*mat2[i,j]
    
    return outputmat
            

def applyConvOnImage(img, customKernel):
    
    if len(img.shape) ==3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    img_height , img_width = img.shape
    outputImg = np.zeros_like(img)
    
    for i in range(1, img_width-1):
        for j in range(1, img_height-1):
            tempMat = img[i-1:i+2 , j-1:j+2]
            convRes = manualConvolution_3x3(tempMat, customKernel)
            outputImg[i,j] = np.sum(convRes) 
            
    
    return outputImg
            
            