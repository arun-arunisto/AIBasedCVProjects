import cv2
import numpy as np
from matplotlib import pyplot as plt

#color enchancement
def equalizeHistColor(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    img[:,:,2] = cv2.equalizeHist(img[:,:,2])
    return cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

img = cv2.VideoCapture(0)
while True:
    _, frame = img.read()
    cap = equalizeHistColor(frame)
    ################Color Transformation##################
    bgr2rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("bgr2rgb", bgr2rgb)
    rgb2bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow('rgb2bgr', rgb2bgr)
    bgr2gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("bgr2gray", bgr2gray)
    rgb2gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('rgb2gray', rgb2gray)
    bgr2hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('bgr2hsv', bgr2hsv)
    rgb2hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    cv2.imshow('rgb2hsv', rgb2hsv)
    bgr2hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    cv2.imshow('bgr2hls', bgr2hls)
    rgb2hls = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
    cv2.imshow('rgb2hls', rgb2hls)
    bgr2xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    cv2.imshow('bg2xyz', bgr2xyz)
    rgb2xyz = cv2.cvtColor(frame, cv2.COLOR_RGB2XYZ)
    cv2.imshow('rgb2xyz', rgb2xyz)
    bgr2lab = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)
    cv2.imshow('bgr2lab', bgr2lab)
    rgb2luv = cv2.cvtColor(frame, cv2.COLOR_RGB2Luv)
    cv2.imshow('rgb2luv', rgb2luv)
    ######################################################
    cv2.imshow("frame", frame)
    cv2.imshow('Histogram Equalisation', cap)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()