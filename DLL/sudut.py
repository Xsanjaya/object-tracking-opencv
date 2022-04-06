import RPi.GPIO as GPIO
import time

servoPIN1 = 17
posisi=0

def position(sudut):
    global posisi
    rotate(sudut,1)
    posisi=sudut
    

def rotate(sudut,delay=0):
    global posisi
    sdt=sudut
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p1 = GPIO.PWM(servoPIN1, 50)
    if sudut>=40:
        tambah=(sudut/10)-4
        sudut+=5+tambah
        
    if sudut>125:
        sudut-=0
    angle=8.8 -(sudut*7/180)
    
    p1.start(angle)
    if delay==0:
        selisih=0
        if sudut>posisi:
            selisih = sudut-posisi
        else:
            selisih= posisi-sudut
        
        delay=selisih/180
        if delay<0.18:
            delay=0.18
        time.sleep(delay)
    else:
        time.sleep(delay)
        
    p1.stop()
    GPIO.cleanup()
    posisi=sdt
    
position(40)