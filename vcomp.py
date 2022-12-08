
import cv2

import numpy as np

def vcomp():
	resim = cv2.imread("its_tanley_bitch.png")
	cv2.imshow("program",resim)
	cv2.waitKey(0)
	cv2.destroyAllWindows()