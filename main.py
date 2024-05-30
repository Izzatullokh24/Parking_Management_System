import cv2
import pickle
import cvzone
import numpy as np


cap = cv2.VideoCapture('carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 106, 46

def checkParkingSpace(imageProcess):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        cv2.rectangle(image, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
        imgCrop = imageProcess[y: y+height, x: x+width]
        #cv2.imshow(str(x*y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        #cvzone.putTextRect(image, str(count), (x, y+height-3), scale=1,
                          # thickness=2, offset=0, colorR=(0,0,255))


        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter+=1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(image, pos, (pos[0] + width, pos[1] + height), color, thickness)
    occupied_spaces = len(posList) - spaceCounter
    cvzone.putTextRect(image, f'Free Space: {spaceCounter} Occupied: {occupied_spaces}', (20, 35), scale=2,
                       thickness=3, offset=10, colorR=(0, 200, 0))
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, image = cap.read()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ImageBlur = cv2.GaussianBlur(imageGray, (3,3), 1)
    ImageThreshold = cv2.adaptiveThreshold(ImageBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY_INV, 25, 16)
    ImageMedian = cv2.medianBlur(ImageThreshold, 5)
    kernel = np.ones((3,3), np.int8)
    imageDilate = cv2.dilate(ImageMedian, kernel, iterations=1)

    checkParkingSpace(imageDilate)
    #for pos in posList:
       # cv2.rectangle(image, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)



    cv2.imshow("Image", image)
    #cv2.imshow('Imageblur', ImageBlur)
    #cv2.imshow('ImageThreshold', ImageThreshold)
   #cv2.imshow('ImageMedian', ImageMedian)
    cv2.waitKey(10)