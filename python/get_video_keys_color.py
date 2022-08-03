import cv2
import numpy as np
import time
import sc_send as scs

#vid = cv2.VideoCapture('vtx250.jpg')
vid = cv2.VideoCapture('starry_night.jpg')
ret, frame_orig = vid.read()
height, width, dim = frame_orig.shape
print( "height = ", height )
print( "width  = ", width  )
print( "dim    = ", dim    )
#frame = frame_orig

scs.FREQ_STEP = 128
NOTE_OFFSET = 0

new_height = int(scs.FREQ_STEP)
new_width  = int(width)
#new_width  = int(width * new_height / height)
frame = cv2.resize(frame_orig, ( new_width, new_height), interpolation = cv2.INTER_LINEAR)

height, width, dim = frame.shape
print( "new height = ", height )
print( "new width  = ", width  )
print( "new dim    = ", dim    )
print(frame.shape)

#img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

scs.FREQ_MIN=400.0
scs.FREQ_MAX=1000.0

scs.init()


f_filt_center = 2000.0
f_filt_swing  = 1500.0
f_filt_width  = 0.05
f_filt_freq   = 0.5

NUM_NOTES = 6

for i in range(width):
  col            = frame[:,i,0]
  col_filt       = frame[:,i,1]
  col_filt_width = frame[:,i,2]
  col_max        = np.argpartition(col, -NUM_NOTES)[-NUM_NOTES:] 
  for j in range(len(col)):
    freq = j
    freq_amp = col[j] / 255.0 / scs.FREQ_STEP

    filt_freq = col_filt[j] / 255.0 * f_filt_center
    filt_width = col_filt_width[j] / 255.0 * f_filt_width
    if( j in col_max ):
      scs.send_note(NOTE_OFFSET+j,freq_amp, 100.0)
      #scs.send_note(NOTE_OFFSET+j,freq_amp, 100.0, filt_freq, filt_width)
    else:
      scs.send_note(NOTE_OFFSET+j,0.0)

    #scs.send(freq,freq_amp, 100.0, filt_freq, filt_width)
    #print(freq, " " , freq_amp)
    print(".",end='')
  print()
  time.sleep(0.1)

scs.off_all()  
