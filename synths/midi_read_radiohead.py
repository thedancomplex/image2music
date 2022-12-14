import mido
import time
import rtmidi
from rtmidi.midiconstants import NOTE_ON, NOTE_OFF


midiout = rtmidi.MidiOut()
#mid  = mido.MidiFile('radiohead-creep.mid')
#mid  = mido.MidiFile('MellonCollieAndTheInfiniteSadness.mid')
mid  = mido.MidiFile('radiohead-creep.mid')
mido.set_backend('mido.backends.rtmidi/LINUX_ALSA')
#mido.Backend('mido.backends.rtmidi/UNIX_JACK')
print(mido.backend)


##port = mido.open_output('USB Uno MIDI Interface MIDI 1')
avaliable_ports = midiout.get_ports()
print(avaliable_ports)
time.sleep(1)
port = midiout.open_port(1)

#ports = mido.get_output_names()
#print(ports)
##port = mido.open_output(ports[0])
#port = mido.open_output()

msg = mido.Message('note_on', note=60)
# port.send(msg)

print(port)
for i in range(128):
  msg = mido.Message('note_off', note=i)
  port.send_message(msg.bytes())
#  port.send(msg)

for i, track in enumerate(mid.tracks):
  print('Track {}: {}'.format(i, track.name))

## print('pause 3 sec')
## time.sleep(3.0)
## print('play')
tps = mido.bpm2tempo(200)
print(tps)

track = mido.MidiTrack()
track.append(mido.MetaMessage('set_tempo', tempo=tps))
#mid.tracks.append(track)


for msg in mid.play():
  print(msg)
  #port.send(msg)
  byt = msg.bytes()
  bbyt = byt[0] & 0b00001111 + 1
  print(bbyt)
  if bbyt == 10:
    port.send_message(msg.bytes())



