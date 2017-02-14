import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(23,GPIO.OUT,initial=GPIO.HIGH)

def callback_btn17(channel):
    GPIO.output(18, GPIO.LOW)
    print "btn1 pressed, activating 18"
    GPIO.output(18, GPIO.HIGH)

def callback_btn27(channel):
    GPIO.output(23, GPIO.LOW)
    print "btn2 pressed, activating 23"
    GPIO.output(23, GPIO.HIGH)

def callback_btn22(channel):
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    print "btn3 pressed, activating both 18 and 23"
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)

GPIO.add_event_detect(27, GPIO.FALLING, callback=callback_btn27,bouncetime=500)
GPIO.add_event_detect(17, GPIO.FALLING, callback=callback_btn17,bouncetime=500)
GPIO.add_event_detect(22, GPIO.FALLING, callback=callback_btn22,bouncetime=500)

while True:
    time.sleep(1e6)
