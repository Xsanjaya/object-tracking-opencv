from servo import *
from camera import *

opencam('haarcascade.xml')

center_x=80
center_y=90
position_x(center_x)
position_y(90)

pos_x=center_x
pos_y=center_y
timer_x=0
timer_y=0

while True:
    hmn,c,im = camstart()
    for (x,y,w,h) in hmn:
            
            if w>160:
                timer_x=0
                print('=============================')
                xm = int(x + (w/2))
                c.line(im,(xm,0),(xm,480),(0,255,0),2)
                
                if xm<325:
                    pos_x-=2
                    rotate_x(pos_x)
                elif xm>395:
                    pos_x+=2
                    rotate_x(pos_x)
                    
            else:
                timer_x+=1
                print('timer_x=' + str(timer_x))
                if timer_x>10 and pos_x!=center_x:
                    rotate_x(center_x)
                    timer_x=0
                    print('=============================')
                    time.sleep(3)
            
            if h>160:
                timer_y=0
                print('=============================')
                ym = int(y + (h/2))
                c.line(im,(0,ym),(720,ym),(0,255,0),2)
                
                if ym<220:
                    pos_y-=2
                    rotate_y(pos_y)
                elif ym>260:
                    pos_y+=2
                    rotate_y(pos_y)
                    
            else:
                timer_y+=1
                print('timer_y=' + str(timer_y))
                if timer_y>10 and pos_y!=center_y:
                    rotate_y(center_y)
                    timer_y=0
                    print('=============================')
                    time.sleep(3)
            showcam(im)
            if waitkey():
                break
        

print('stop')        
camstop()
