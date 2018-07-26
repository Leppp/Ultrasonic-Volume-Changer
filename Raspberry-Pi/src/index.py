import RPi.GPIO as GPIO
import time
from rx import Observable, Observer
import socket
import json 

UDP_IP = '10.40.142.222'
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
    while len(dist) < 4:
        dist.append(distance)
    dist.remove(max(dist))
    dist.remove(min(dist))
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

Observable.interval(25)\
    .map(lambda i: distance())\
    .scan(lambda acc, x: (x + (acc - ((x + (acc -x))/2)))/2)\
    .subscribe(NetworkObserver())

input('')
