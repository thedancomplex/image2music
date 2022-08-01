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

def send(note_index=None, note_amp=None):
  if note_index == None:
    return 1
  if note_amp == None:
    return 1

  df = (FREQ_MAX - FREQ_MIN) / FREQ_STEP

  pre   = '/key'
  post  = str(note_index)
  final = pre+post
  freq  = df * note_index
  client.send_message(final, (freq, note_amp)) # set the frequency at 440

  return 0


def send_note_major(note_index=None, note_amp=None):
  if note_index == None:
    return 1
  if note_amp == None:
    return 1



def send_note(note_index=None, note_amp=None):
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
  client.send_message(final, (freq, note_amp)) # set the frequency at 440
  return 0
