import RPi.GPIO as GPIO
import time

servo_x = 17
servo_y = 18
posisi_x=0
posisi_y=0

def position_x(sudut):
    global posisi_x
    rotate_x(sudut,1)
    posisi_x=sudut
    

def rotate_x(sudut,delay=0):
    global posisi_x
    sdt=sudut
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo_x, GPIO.OUT)
    px = GPIO.PWM(servo_x, 50)
    
    if sudut>=40:
        tambah=(sudut/10)-4
        sudut+=5+tambah
        
    if sudut>125:
        sudut-=0
    angle=8.8 -(sudut*7/180)
    
    px.start(angle)
    
    if delay==0:
        selisih=0
        if sudut>posisi_x:
            selisih = sudut-posisi_x
        else:
            selisih= posisi_x-sudut
        
        delay=selisih/180
        if delay<0.18:
            delay=0.18
        time.sleep(delay)
    else:
        time.sleep(delay)
        
    px.stop()
    GPIO.cleanup()
    posisi_x=sdt
    
    
def position_x(sudut):
    global posisi_x
    rotate_x(sudut,1)
    posisi_x=sudut
    

def rotate_x(sudut,delay=0):
    global posisi_x
    sdt=sudut
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo_x, GPIO.OUT)
    px = GPIO.PWM(servo_x, 50)
    
    if sudut>=40:
        tambah=(sudut/10)-4
        sudut+=5+tambah
        
    if sudut>125:
        sudut-=0
    angle=8.8 -(sudut*7/180)
    
    px.start(angle)
    
    if delay==0:
        selisih=0
        if sudut>posisi_x:
            selisih = sudut-posisi_x
        else:
            selisih= posisi_x-sudut
        
        delay=selisih/180
        if delay<0.18:
            delay=0.18
        time.sleep(delay)
    else:
        time.sleep(delay)
        
    px.stop()
    GPIO.cleanup()
    posisi_x=sdt
    
def position_y(sudut):
    global posisi_y
    rotate_y(sudut,1)
    posisi_y=sudut
    

def rotate_y(sudut,delay=0):
    global posisi_y
    sdt=sudut
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo_y, GPIO.OUT)
    py = GPIO.PWM(servo_y, 50)
    
    if sudut>=40:
        tambah=(sudut/10)-4
        sudut+=5+tambah
        
    if sudut>125:
        sudut-=0
    angle=8.8 -(sudut*7/180)
    
    py.start(angle)
    
    if delay==0:
        selisih=0
        if sudut>posisi_y:
            selisih = sudut-posisi_y
        else:
            selisih= posisi_y-sudut
        
        delay=selisih/180
        if delay<0.18:
            delay=0.18
        time.sleep(delay)
    else:
        time.sleep(delay)
        
    py.stop()
    GPIO.cleanup()
    posisi_y=sdt
    
