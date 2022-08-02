import mido
import time
import rtmidi
midiout = rtmidi.MidiOut()
mid  = mido.MidiFile('radiohead-creep.mid')
mido.set_backend('mido.backends.rtmidi/LINUX_ALSA')
#mido.Backend('mido.backends.rtmidi/UNIX_JACK')
print(mido.backend)


#port = mido.open_output('USB Uno MIDI Interface MIDI 1')
#avaliable_ports = midiout.get_ports()
#print(avaliable_ports)
#port = midiout.open_port(0)

ports = mido.get_output_names()
print(ports)
#port = mido.open_output(ports[0])
port = mido.open_output()

msg = mido.Message('note_on', note=60)
# port.send(msg)

print(port)
for i in range(128):
  msg = mido.Message('note_off', note=i)
#  port.send_message(msg)
  port.send(msg)

for i, track in enumerate(mid.tracks):
  print('Track {}: {}'.format(i, track.name))

## print('pause 3 sec')
## time.sleep(3.0)
## print('play')
for msg in mid.play():
  print(msg)
  port.send(msg)
  #port.send_message(msg)



