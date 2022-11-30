import cv2
import pytesseract

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #print(frame.shape)
    hImg, wImg, _ = frame.shape
    #print(len(pytesseract.image_to_string(frame)))
    boxes = pytesseract.image_to_data(frame)
    print(pytesseract.get_languages())
    #print(boxes)
    for x,b in enumerate(boxes.splitlines()):
        #print(b)
        if x!=0:
            b = b.split()
            #print(b)
            print(len(b))
            if len(b) == 12 and b[6] != 'left':
                print(b[6])
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(frame, (x, y), (w+x, h+y), (0, 0, 255), 1)
                cv2.putText(frame, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                print(b[11])

        """if b[1] != '0':
            cv2.imshow('gray', gray)
        else:"""
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        print("exit")
        break
cv2.destroyAllWindows()