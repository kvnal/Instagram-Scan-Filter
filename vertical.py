import cv2 as cv

video = cv.VideoCapture(0)

four_cc = cv.VideoWriter_fourcc(*'XVID')
output=cv.VideoWriter('saved.avi',four_cc,20.0,(640,480))

ret , frame = video.read()
h,w=frame.shape[:2]
frame2=frame.copy()

px=1

for _ in range(0,w,px):
    frame2[0:h,_:_+px]=frame[0:h,_:_+px]
    frame[0:h,0:_+px]=frame2[0:h,0:_+px] 
    cv.line(frame,(_,0),(_,h),(218,227,108),5)
    output.write(frame)
    cv.imshow('filter',frame)
    ret , frame  = video.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.imwrite('saved.png',frame2)
video.release()
output.release()
cv.destroyAllWindows()
