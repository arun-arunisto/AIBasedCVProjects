import PyPDF2
import cv2 as cv
import pytesseract

img = cv.imread('sample12.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))
"""hImg, wImg, _ = img.shape
print(img.shape)
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    #print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv.rectangle(img,(x, hImg-y),(w, hImg-h),(0,0,255),1)
    cv.putText(img,b[0],(x, hImg-y+25), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
"""

#detecting words
hImg, wImg, _ = img.shape
print(img.shape)
boxes = pytesseract.image_to_data(img)
print(boxes)

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv.rectangle(img,(x, y),(w+x, h+y),(0,0,255),1)
            cv.putText(img,b[11],(x, y), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)


#detecting numbers
"""hImg, wImg, _ = img.shape
con = r' --oem 3 --psm 6 outputbase digits'
print(img.shape)
boxes = pytesseract.image_to_data(img, config=con)
print(boxes)

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv.rectangle(img,(x, y),(w+x, h+y),(0,0,255),1)
            cv.putText(img,b[11],(x, y), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
"""
cv.imshow('img', img)
cv.waitKey(0)


