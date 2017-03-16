import RPi.GPIO as GPIO
import time
import threading
import os
GPIO.setmode(GPIO.BCM) #use BCM numbering scheme

#map buttons to BCM pins per PinOut.md
DictIn = {1:17,2:27,3:22,4:5,5:6}
DictOut = {'A':18,'B':23,'C':24,'Z':25}

for key in DictIn:
    GPIO.setup(DictIn[key], GPIO.IN, pull_up_down=GPIO.PUD_UP)

for key in DictOut:
    GPIO.setup(DictOut[key], GPIO.OUT, initial=GPIO.HIGH)


GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) #setup power on indicator light
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setup shutdown button

#map BCM button inputs to BCM Wiimote outputs
comboLookup = {17:[18],27:[23],22:[18,23],5:[24],6:[25]}  

def thread_outputMacro(pin):
    GPIO.output(comboLookup[pin],GPIO.LOW)
    print "pulling",  "low"
    time.sleep(0.25)
    GPIO.output(comboLookup[pin],GPIO.HIGH)
    print "returning",  "high"

def callback_btnPress(pin):
    #GPIO.output(18, GPIO.LOW)
    print "btn %d pressed" % pin
    t=threading.Thread(target=thread_outputMacro, args=(pin,),name="macroThread")
    t.start()
    #GPIO.output(18, GPIO.HIGH)

def callback_btnShutdown(pin):
    GPIO.cleanup()           # clean up GPIO on shutdown
    os.system("sudo shutdown -h now")

#def callback_btn27(channel):
#    GPIO.output(23, GPIO.LOW)
#    print "btn2 pressed, activating 23"
#    GPIO.output(23, GPIO.HIGH)
#
#def callback_btn22(channel):
#    GPIO.output(18, GPIO.LOW)
#    GPIO.output(23, GPIO.LOW)
#    print "btn3 pressed, activating both 18 and 23"
#    GPIO.output(18, GPIO.HIGH)
#    GPIO.output(23, GPIO.HIGH)

for key in DictIn:
    GPIO.add_event_detect(DictIn[key], GPIO.FALLING, callback=callback_btnPress,bouncetime=500)

GPIO.add_event_detect(26, GPIO.RISING, callback=callback_btnShutdown, bouncetime=500)

GPIO.output(21,GPIO.HIGH)

try:
    while True:
        time.sleep(1e6)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

