#CamCoder


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
filename = str(input("Enter The name of your file"))+'.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(filename,fourcc, 24.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        
        out1.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out1.release()
cv2.destroyAllWindows()
