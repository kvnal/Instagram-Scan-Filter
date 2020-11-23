import cv2 as cv

video = cv.VideoCapture(0)


ret , frame = video.read()
h,w=frame.shape[:2]
frame2=frame.copy()

four_cc = cv.VideoWriter_fourcc(*'XVID')
output=cv.VideoWriter('saved.avi',four_cc,20.0,(640,480))

px=1 

for _ in range(0,h,px):
    frame2[_:_+px,0:w]=frame[_:_+px,0:w]
    frame[0:_+px,0:w]=frame2[0:_+px,0:w]
    cv.line(frame,(0,_),(w,_),(218,227,108),5)
    cv.imshow('filter',frame)
    output.write(frame)
    ret , frame  = video.read()
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cv.imwrite('saved.png',frame2)
video.release()
output.release()
cv.destroyAllWindows()
