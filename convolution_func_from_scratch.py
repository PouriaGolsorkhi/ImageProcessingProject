import cv2
import matplotlib.pyplot as plt
import numpy as np

def manualConvolution_3x3(mat1, mat2):
    
    return np.sum(mat1*mat2);
            

def applyConvOnImage(img, customKernel):
    

        
    img_height , img_width, dimensions = img.shape
    outputImg = np.zeros_like(img)
    paded_image = np.pad(img, ((1,1), (1,1), (0,0)), mode="constant")
    for i in range(1, img_width):
        for j in range(1, img_height):
            for k in range(dimensions):
                tempMat = paded_image[i-1:i+2 , j-1:j+2, k]
                convRes = manualConvolution_3x3(tempMat, customKernel)
                outputImg[i,j,k] = np.sum(convRes) 
            
    outputImg = np.clip(outputImg, 0, 255).astype(np.uint8)
    
    return outputImg
            
            