# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 13:50:24 2018

@author: d4gamba
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    for row in laplacian:
        row[0][0]=250
        row[0][1]=250
        row[0][2]=250
        row[1][0]=250
        row[1][1]=250
        row[1][2]=250
        row[2][0]=0
        row[2][1]=0
        row[2][2]=0
        row[3][0]=0
        row[3][1]=0
        row[3][2]=0

    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

