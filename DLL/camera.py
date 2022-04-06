import cv2
cam = cv2.VideoCapture(0)
# vid_cod = cv2.VideoWriter_fourcc(*'MPEG')
# output = cv2.VideoWriter("cam_video.mp4", vid_cod, 20.0, (640,480))
def opencam(mode):
    global human_cascade
    human_cascade = cv2.CascadeClassifier(mode)
    #'haarcascade_frontalface_default.xml'
    

def camstart():
    ret, image = cam.read()
    hsv_frame = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    humans = human_cascade.detectMultiScale(hsv_frame,1.9,1)
        
    return humans,cv2,image


def camstop():
    cam.release()
#     output.release()
    cv2.destroyAllWindows()
    
def cobalah():
    return 1,2,3

def showcam(image):
    cv2.imshow('Imagetest',image)
#     output.write(image)
    
def waitkey():
    k = cv2.waitKey(1)
    if k != -1:
        return True
