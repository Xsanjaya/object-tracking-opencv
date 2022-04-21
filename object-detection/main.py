import numpy as np
import cv2 as cv
from servo import *

center_x=80
center_y=90
position_x(center_x)
position_y(90)

pos_x=center_x
pos_y=center_y
timer_x=0
timer_y=0

cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'X264')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
humman_object = cv.CascadeClassifier('library.xml')

while cap.isOpened():
	ret, frame = cap.read()
	median = cv.medianBlur(frame, 5)
	hsv_frame = cv.cvtColor(median,cv.COLOR_BGR2HSV)
	humans = humman_object.detectMultiScale(hsv_frame,1.9,1)
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	for (x,y,w,h) in humans:
		if w>160:
			timer_x=0
			
			xm = int(x + (w/2))
			cv.line(frame,(xm,y),(xm,y+h),(0,255,0),2)
			
			if xm<325:
					pos_x-=2
					rotate_x(pos_x)
			elif xm>395:
					pos_x+=2
					rotate_x(pos_x)
					
		else:
			timer_x+=1
			
			if timer_x>10 and pos_x!=center_x:
					rotate_x(center_x)
					timer_x=0
					
					time.sleep(3)
		
		if h>160:
			timer_y=0
			
			ym = int(y + (h/2))
			cv.line(frame,(x,ym),(x+w,ym),(0,255,0),2)
			cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			if ym<220:
					pos_y-=2
					rotate_y(pos_y)
			elif ym>260:
					pos_y+=2
					rotate_y(pos_y)
					
		else:
			timer_y+=1
			
			if timer_y>10 and pos_y!=center_y:
					rotate_y(center_y)
					timer_y=0
					
					time.sleep(3)
	# write the flipped frame
	out.write(frame)
	cv.imshow('frame', frame)
	if cv.waitKey(1) == ord('q'):
		break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()