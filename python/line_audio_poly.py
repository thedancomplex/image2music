from pythonosc import udp_client
import time

client = udp_client.SimpleUDPClient("127.0.0.1", 57120) #default ip and port for SC

f = 450
#while True:
f = f + f/100.0
 # client.send_message('/key0', f) # set the frequency at 440
 # client.send_message('/key1', f/2.0) # set the frequency at 440
#client.send_message('/key0', (400, 0)) # set the frequency at 440
client.send_message('/key127', (410, 0)) # set the frequency at 440
#client.send_message('/key1', 200) # set the frequency at 440
#client.send_message('/key2', 500) # set the frequency at 440
#client.send_message('/key3', 1000) # set the frequency at 440
#client.send_message('/key4', 2000) # set the frequency at 440
#client.send_message('/key5', 5000) # set the frequency at 440
#  break
time.sleep(0.5)
