"""EE 250L Lab 04 Custom Code 
	vm_start_chain.py"""

# Github Repo Link: https://github.com/jessicazhu318/lab-04.git

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    
    print("Connected to server (i.e., broker) with result code "+str(rc))
    
    # subscription to pong
    client.subscribe("zhujessi/pong")
    # custom callback
    client.message_callback_add("zhujessi/pong", on_message_from_pong)
 
def on_message(client, userdata, msg): 
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_from_pong(client, userdata, msg):

    print("Custom callback  - Pong: "+ msg.payload.decode())
    
    # converts number to int and adds 1
    number = int(msg.payload)
    nextNumber = number + 1
    
    # publish ping
    client.publish("zhujessi/ping", f"{nextNumber}")
    print("Publishing number")
    time.sleep(1)

if __name__ == '__main__':

    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    # connect to rpi
    client.connect(host="172.20.10.4", port=1883, keepalive=60)

    client.loop_start()
    time.sleep(1)

    while True:
    
    	# ask for starting number
        number = int(input("Enter a starting number: "))
        
        # publish starting number as ping
        client.publish("zhujessi/ping", f"{number}")
        print("Publishing number")
        time.sleep(1)
        

