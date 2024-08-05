import cv2
import matplotlib.pyplot as plt
import numpy as np

def manualConvolution_3x3(mat1, mat2):
    outputmat = [[1 for y in mat1[0]] for x in mat1]
    
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        raise ValueError("mat1 and mat2 must have the same dimensions")
    
    
    for i in range(0,len(mat1)):
        for j in range(0,len(mat1[i])):
            outputmat[i][j] = mat1[i][j]*mat2[i][j]
    
    return outputmat
            

def applyConvOnImage(img, customKernel):
    for i in range(1, img.shape[1], 3):
        for j in range(1, img.shape[0], 3):
            tempMat = img[i-1:i+2][j-1:j+2]
            img[i-1:i+2][j-1:j+2] = manualConvolution_3x3(tempMat , customKernel)
    
    return img
            
            