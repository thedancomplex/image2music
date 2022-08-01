import cv2
import numpy as np
import time
import sc_send as scs

vid = cv2.VideoCapture('vtx250.jpg')
ret, frame_orig = vid.read()
height, width, dim = frame_orig.shape
print( "height = ", height )
print( "width  = ", width  )
print( "dim    = ", dim    )
#frame = frame_orig
new_height = int(128)
new_width  = int(width * new_height / height)
frame = cv2.resize(frame_orig, ( new_width, new_height), interpolation = cv2.INTER_LINEAR)

height, width, dim = frame.shape
print( "new height = ", height )
print( "new width  = ", width  )
print( "new dim    = ", dim    )
print(frame.shape)

img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

scs.init()

for i in range(width):
  col = img_gray[:,i]
  for j in range(len(col)):
    freq = j
    freq_amp = col[j] / 255.0 / scs.FREQ_STEP * 10.0 
    scs.send(freq,freq_amp)
    print(freq, " " , freq_amp)
  time.sleep(0.1)
  
