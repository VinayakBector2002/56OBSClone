import numpy as np
import cv2
import pyscreenshot as pys
import datetime

current_time = str(input("Enter name of your file : "))
name= str((current_time+".avi"))
print("started recording",name)
forcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(name, forcc, 1.0, (1920,1080))


while True:
    img= pys.grab()
    img_np=np.array(img)

    img_np=cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    cv2.imshow('Screen', img_np)
    out.write(img_np)


    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
