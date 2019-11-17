import RPi.GPIO as gpio
from gpiozero import LED
from signal import pause
from time import sleep


import sys
import socket


server_addr = ("10.42.0.1", 7777)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connection to %s:%d"%server_addr)
sock.connect(server_addr)


upPin = 4
downPin = 26


while True: 
    gpio.setmode(gpio.BCM)
    gpio.setup(upPin, gpio.IN)
    gpio.setup(downPin, gpio.IN)

    msg = sock.recv(255)
    print("recvd: %s"%msg)

    pin = 0
    if msg == b"up":
        pin = upPin
    elif msg == b"down":
        pin = downPin
    if pin:
        gpio.setup(pin,gpio.OUT)
        gpio.output(pin, gpio.LOW)

        sleep(1)
        print("setting pin %d to INPUT"%pin)
        gpio.output(pin, gpio.HIGH)
        gpio.setup(pin, gpio.IN)
    gpio.cleanup()
