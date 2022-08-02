import rtmidi
from rtmidi.midiconstants import NOTE_ON, NOTE_OFF
import time
import os

midi_out = rtmidi.MidiOut()
avaliable_ports = midi_out.get_ports()

midi_out.open_port(1)
print(midi_out.is_port_open())

while midi_out:
  midi_out.send_message([NOTE_ON, 60, 100])
#  os.system('sync')
  print('.', end='', flush=True)
  time.sleep(0.1)
  midi_out.send_message([NOTE_OFF, 60, 0])
#  os.system('sync')
  print('.', end='', flush=True)
  time.sleep(0.1)

