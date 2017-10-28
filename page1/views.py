from django.shortcuts import render,HttpResponse
import RPi.GPIO as GPIO
import time
# Create your views here.

def index(request):
    print(request.POST)
    if request.POST['switch']:
        pin4(request.POST['switch'])
    return render(request, 'page1.html', {'request':request})


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def pin4(mode=False):
    while mode:
        GPIO.output(4, True)


##GPIO.output(4, False)

##GPIO.cleanup()

##GPIO.setmode(GPIO.BCM)
##GPIO.setup(4,GPIO.IN)

##for i in range(10000):
##    time.sleep(0.05)
##    print(GPIO.input(4))

GPIO.cleanup()