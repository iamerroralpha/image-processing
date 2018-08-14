# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:32:14 2018

@author: d4gamba
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 13:50:24 2018

@author: d4gamba
"""

import cv2
import numpy as np
import copy

cap = cv2.VideoCapture(0)
red = 0
green = 1
blue = 2
do = 1
b_red=0
b_blue=0
b_green=0
while(do):

    # Take each frame
    _, frame = cap.read()
    frame2 = copy.deepcopy(frame)
    frameRGB = copy.deepcopy(frame)
    frameRGb = copy.deepcopy(frame)
    frameRgB = copy.deepcopy(frame)
    frameRgb = copy.deepcopy(frame)
    framerGB = copy.deepcopy(frame)
    framerGb = copy.deepcopy(frame)
    framergB = copy.deepcopy(frame)
    framergb = copy.deepcopy(frame)
    
    
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    
    
    for index_row,row in enumerate(frame):
        for index_column,column in enumerate(row):
            b_red   = 255 - column[red]
            b_green = 255 - column[green]
            b_blue  = 255 - column[blue]
            
            frameRGb[index_row][index_column][blue] = b_blue
            
            frameRgB[index_row][index_column][green] = b_green
            
            frameRgb[index_row][index_column][blue] = b_blue
            frameRgb[index_row][index_column][green] = b_green
            
            framerGB[index_row][index_column][red] = b_red
            
            framerGb[index_row][index_column][red] = b_red
            framerGb[index_row][index_column][blue] = b_blue
            
            framergB[index_row][index_column][red] = b_red
            framergB[index_row][index_column][green] = b_green
            
            framergb[index_row][index_column][red] = b_red
            framergb[index_row][index_column][green] = b_green
            framergb[index_row][index_column][blue] = b_blue

    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('frameRGB',frameRGB)
    cv2.imshow('frameRGb',frameRGb)
    cv2.imshow('frameRgB',frameRgB)
    cv2.imshow('frameRgb',frameRgb)
    cv2.imshow('framerGB',framerGB)
    cv2.imshow('framerGb',framerGb)
    cv2.imshow('framergB',framergB)
    cv2.imshow('framergb',framergb)
    
    do = 0
    
while(1):
    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('frameRGB',frameRGB)
    cv2.imshow('frameRGb',frameRGb)
    cv2.imshow('frameRgB',frameRgB)
    cv2.imshow('frameRgb',frameRgb)
    cv2.imshow('framerGB',framerGB)
    cv2.imshow('framerGb',framerGb)
    cv2.imshow('framergB',framergB)
    cv2.imshow('framergb',framergb)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
      break
  
cv2.destroyAllWindows()
cap.release()

