
import cv2

import numpy as np

def vcomp():
	#image = cv2.imread("its_tanley_bitch.png",0)
	#print(image)
	#cv2.imshow("program",image)
	camera = cv2.VideoCapture(0)
	while True:
		ret, frame = camera.read()
		cv2.imshow("video",frame)
		if cv2.waitKey(10) & 0xFF == ord("q"):
			break
	camera.release()
	cv2.destroyAllWindows()