#import library openCV untuk object detection
import cv2 as cv
#import fungsi servo pada file local
from servo import *

#menentukan posisi tengah servo x
center_x=80
#menentukan posisi tengah servo y
center_y=90

#menggerakkan servo x dan y ke pada posisi tengah
position_x(center_x)
position_y(center_y)

#mencatat posisi sudut terakhir pada tiap servo
pos_x=center_x
pos_y=center_y

#variabel pembatasan waktu agar servo kembali ke posisi awal sat tidak mendeteksi objek
    #batas
batas_x=10
batas_y=10
    #counter
timer_x=batas_x
timer_y=batas_y

cap = cv.VideoCapture(0)
#mengatur encoder dan memulai menulis video
fourcc = cv.VideoWriter_fourcc(*'X264')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

#mode cascade ( disini pakai deteksi wajah )
human_cascade = cv.CascadeClassifier('library.xml')

while cap.isOpened():
    #baca frame dari tangkapan webcam
    ret, frame = cap.read()
    #frame hsv untuk object deteksi
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    #filter sesuai objek yang ditentukan ( wajah manusia )
    humans = human_cascade.detectMultiScale(hsv_frame,1.9,1)
    
    #bila tidak ada tangkapan dari webcam / webcam tidak terpasang maka program akan berhenti 
    if not ret:
        print("Pastikan camera telah terpasang")
        break
    
    #cek setiap objek yang terdeteksi ( wajah manusia )
    for (x,y,w,h) in humans:
        #ambil objek dengan lebar lebih dari 160px
        if w>160:
            #atur pembatasan waktu deteksi ke posisi semula saat objek terdeteksi
            timer_x=batas_x
            
            #mendapatkan garis tengah untuk servo x sebagai poros utk mendapatkan perubahan nilai pergerakan horisontal
            xm = int(x + (w/2))
            cv.line(frame,(xm,y),(xm,y+h),(0,255,0),2)
            #bila posisi objek kurang dari 325px maka sudut servo x dikurangi
            if xm<325:
                pos_x-=2
                rotate_x(pos_x)
            #bila posisi objek lebih dari 395px maka sudut servo x ditambah
            elif xm>395:
                pos_x+=2
                rotate_x(pos_x)
                
        else:
            #pembatasan waktu dikurangi 1 saat tidak ditemukan objek pada setiap objek
            timer_x-=1
            
            #saat nilai pembatasan waktu = 0 maka posisi servo x dikembalikan ke posisi tengah, dan pembatas waktu diset ke batas awal
            if timer_x==0 and pos_x!=center_x:
                rotate_x(center_x)
                timer_x=batas_x
                
                time.sleep(3)
        #ambil objek dengan tinggi lebih dari 160px
        if h>160:
            #atur pembatasan waktu deteksi ke posisi semula saat objek terdeteksi
            timer_y=batas_y
            
            #mendapatkan garis tengah untuk servo y sebagai poros utk mendapatkan perubahan nilai pergerakan vertikal
            ym = int(y + (h/2))
            cv.line(frame,(x,ym),(x+w,ym),(0,255,0),2)
            #memberi persegi warna biru pada objek
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            
            #bila posisi objek kurang dari 220px maka sudut servo xy dikurangi
            if ym<220:
                pos_y-=2
                rotate_y(pos_y)
            #bila posisi objek lebih dari 260px maka sudut servo y ditambah
            elif ym>260:
                pos_y+=2
                rotate_y(pos_y)
                
        else:
            #pembatasan waktu dikurangi 1 saat tidak ditemukan objek pada setiap objek
            timer_y+=1
            #saat nilai pembatasan waktu = 0 maka posisi servo x dikembalikan ke posisi tengah, dan pembatas waktu diset ke batas awal
            if timer_y==10 and pos_y!=center_y:
                rotate_y(center_y)
                timer_y=batas_y
                
                time.sleep(3)
    #menambah frame ke dalam penulisan video
    out.write(frame)
    #menampilkan frame pada form video ( penampil video webcam)
    cv.imshow('frame', frame)
    # write the flipped frame
    
    #tutup program saat tekan tombol 1 atau q
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
#matikan camera dan video writer
cap.release()
out.release()
cv.destroyAllWindows()