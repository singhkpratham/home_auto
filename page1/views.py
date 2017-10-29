from django.shortcuts import render,HttpResponse
import RPi.GPIO as GPIO
import time
# Create your views here.
pins = list([1,2,3,4])
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

def index(request):
    if request.method == 'POST':
        dt = dict(request.POST)
        pinsOn  = [int(k[-1]) for k in dt if k[:3] == 'pin']
        pinsOff = [c for c in pins if c not in pinsOn]
        GPIO.output(pinsOn, GPIO.HIGH)
        GPIO.output(pinsOff, GPIO.LOW)
    # print(pinsOff,pinsOn)
    pinStatus = {p:'checked' if GPIO.input(p) == 1 else '' for p in pins }
    print(pinStatus)
    return render(request, 'page1.html', {'request':request,'pins':pinStatus})


# TODO: 1. add specific time and timer to start the pins. this will most probably require threading
# TODO: 2. login page, only registered users can log in and turn pins on/off
