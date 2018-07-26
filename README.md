# Ultrasonic-Volume-Changer
Allows you to change the volume on your computer using your hand and an ultrasonic sensor

# What you will need:
- A Raspberry Pi
- A computer on which to change the volume
- An Ultrasonic Sensor (http://www.dx.com/p/hc-sr04-ultrasonic-sensor-distance-measuring-module-133696#.W1oGvIAnbRY)
- A breadboard
- Wires

# How to install:
The *Raspberry-Pi* folder contains the files to use with the Raspberry-Pi, and the *Main-Device* folder the files to use with your main device.

# How to run
On your Raspberry-Pi, open the file index.py and change those variables:
- UDP_IP
- UDP_PORT

Then, execute the command:
<python index.py>

On your main device, simply execute the command:
<npm run start>

# How to use:
Simply put your hand over the ultrasonic sensor, and move it up to raise the volume, or move it down to lower it.
