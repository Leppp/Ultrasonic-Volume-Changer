import RPi.GPIO as GPIO
import time
from rx import Observable, Observer
import socket
import json 

UDP_IP = 'ip of your main device' # put the ip of your main device here
UDP_PORT = 5000

GPIO.setmode(GPIO.BCM)
 
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    dist = []
    while len(dist) < 4: # creates a list with 3 values of distance
        dist.append(distance)
    dist.remove(max(dist)) # removes the highest value
    dist.remove(min(dist)) # removes the lowest value
    distance = dist[0] 
    return distance

class NetworkObserver(Observer):

    def __init__(self, host = 'localhost', port = 5000):
        super(NetworkObserver, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port

    def on_next(self, value):
        self.sock.sendto(json.dumps({'distance': value})+'\n', (UDP_IP, UDP_PORT))
    
    def on_error(self, error):
        pass

    def on_completed(self):
        pass

Observable.interval(25)\ # you can change the interval value (default: 25)
    .map(lambda i: distance())\
    .scan(lambda acc, x: (x + (acc - ((x + (acc -x))/2)))/2)\ # the goal of this .scan is to smooth up the values
    .subscribe(NetworkObserver())

input('')
