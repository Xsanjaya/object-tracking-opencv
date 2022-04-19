import cv2

vidCap=cv2.VideoCapture(0)
vidCap.set(3, 1280)
vidCap.set(4, 720)
count = 1
while True :
	_,vidOri = vidCap.read()
	vidHSV = cv2.cvtColor(vidOri, cv2.COLOR_BGR2HSV)

	cv2.imshow("Video Ori",vidOri)
	cv2.imshow("video HSV", vidHSV)

	k=cv2.waitKey(1) & 0xFF
	if (k==27):               #tekan esc untuk keluar
		vidCap.release()
		cv2.destroyAllWindows()
		break

	if k == ord('s'):
		file_name1 = 'img/Ori_'+str(count)+'.jpg'
		file_name2 = 'img/Grey_'+str(count)+'.jpg'
		count = count+1

		# simpan image di folder yang aktif sekarang
		cv2.imwrite(file_name1, vidOri)
		cv2.imwrite(file_name2, vidHSV)
		print ("Image", file_name1, file_name2, "Telah Tersimpan")
