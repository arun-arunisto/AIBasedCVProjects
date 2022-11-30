import cv2 as cv
"""
cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    cv.imshow('Frame', frame)
    if cv.waitKey(1) == ord('q'):
        cv.imwrite('test1.jpg', frame)
        break
cv.destroyAllWindows()
"""

import easyocr
"""
def easyText(img):
    reader = easyocr.Reader(['ta', 'en'])
    result = reader.readtext(img)

    print(result)
    for i in result:
        print(i)
    for i in result:
        for j in range(len(i)):
            print(i[j])
        #print(i[-2], end=" ")
    #df = pd.DataFrame(result)
    #print(df[1])
easyText("ss.png")
"""

import PyPDF2
"""
pdffile = open('ps.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffile)

print(pdfreader.numPages) #umber of pages in a pdf file

page = pdfreader.getPage(16)
#print(page)
print(page.extractText())

pdffile.close()
"""