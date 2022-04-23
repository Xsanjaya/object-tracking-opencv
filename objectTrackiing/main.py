import numpy as np, time
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
now = time.strftime("%A_%d_%b_%Y-%H_%M")
fourcc = cv.VideoWriter_fourcc(*'X264')
out = cv.VideoWriter("data/"+now+'.avi', fourcc, 20.0, (640,  480))
object_target = cv.CascadeClassifier('lib/face.xml')

while cap.isOpened():
	ret, frame = cap.read()
	frame_target = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	react = object_target.detectMultiScale(frame_target,1.9,1)
	
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	
	if len(react) >= 1:
		for (x,y,w,h) in react[0]:
			center_coordinates = x + w // 2, y + h // 2
			radius = w // w
			cv.circle(frame, center_coordinates, radius, (255,0,0), 10)
			# cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)

			if w>160:
				timer_x=0
				xm = int(x + (w/2))
				# cv.line(frame,(xm,y),(xm,y+h),(0,255,0),2)
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
				# cv.line(frame,(x,ym),(x+w,ym),(0,255,0),1)
				
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