from pythonosc import udp_client
import time
import note_freq as nf

FREQ_MIN  = 20.0
FREQ_MAX  = 8000.0
FREQ_STEP = 128.0
client = None

def init(ip="127.0.0.1", port=57120):
  global client 
  client = udp_client.SimpleUDPClient(ip, port) #default ip and port for SC
  return 0

def off_all():
  ret = 0
  for i in range(int(FREQ_STEP)):
    ret += send(i, 0.0)
  if ret > 0:
    return 1
  return 0

def send(note_index=None, note_amp=None, post_gain=1.0, filter_freq=None, filter_width=None):
  global client 
  if note_index == None:
    return 1
  if note_amp == None:
    return 1

  pre   = '/key'
  post  = str(note_index)
  final = pre+post
  freq  = get_freq(note_index)
  if(filter_freq == None):
    client.send_message(final, (freq, note_amp*post_gain)) # set the frequency at 440
  elif(filter_width==None):
    client.send_message(final, (freq, note_amp*post_gain, filter_freq)) # set the frequency at 440
  else:
    client.send_message(final, (freq, note_amp*post_gain, filter_freq, filter_width)) # set the frequency at 440

  return 0

def get_freq(note_index=None):
  if note_index == None:
    return -1
  df = (FREQ_MAX - FREQ_MIN) / FREQ_STEP
  freq  = df * note_index + FREQ_MIN
  return freq

def send_note_major(note_index=None, note_amp=None, post_gain=1.0, key_index=0):
  if note_index == None:
    return 1
  if note_amp == None:
    return 1



#def send_note(note_index=None, note_amp=None, post_gain=1.0):
def send_note(note_index=None, note_amp=None, post_gain=1.0, filter_freq=None, filter_width=None):
  global client 
  if note_index == None:
    return 1
  if note_amp == None:
    return 1

  pre   = '/key'
  post  = str(note_index)
  final = pre+post
  freq  = None
  try:
    freq = nf.NOTES[note_index]
  except:
    return 1
  if(filter_freq == None):
    client.send_message(final, (freq, note_amp*post_gain)) # set the frequency at 440
  elif(filter_width==None):
    client.send_message(final, (freq, note_amp*post_gain, filter_freq)) # set the frequency at 440
  else:
    client.send_message(final, (freq, note_amp*post_gain, filter_freq, filter_width)) # set the frequency at 440
  return 0
