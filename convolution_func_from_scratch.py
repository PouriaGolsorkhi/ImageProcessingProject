import cv2
import matplotlib.pyplot as plt
import numpy as np

def manualConvolution_3x3(mat1, mat2):
    
    return np.sum(mat1*mat2);
            

def applyConvOnImage(img, customKernel):
    
    # if len(img.shape) ==3:
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    img_height , img_width, dimensions = img.shape
    outputImg = np.zeros_like(img)
    
    for i in range(1, img_width-1):
        for j in range(1, img_height-1):
            for k in range(dimensions):
                tempMat = img[i-1:i+2 , j-1:j+2, k]
                convRes = manualConvolution_3x3(tempMat, customKernel)
                outputImg[i,j,k] = np.sum(convRes) 
            
    
    return outputImg
            
            