import RPi.GPIO as GPIO
import time
import threading
import os
GPIO.setmode(GPIO.BCM) #use BCM numbering scheme




DictIn = {1:17,2:27,3:22,4:5,5:6,6:26}
DictOut = {'A':18,'B':23,'C':24,'Z':25}

for key in DictIn:
    GPIO.setup(DictIn[key], GPIO.IN, pull_up_down=GPIO.PUD_UP)

for key in DictOut:
    GPIO.setup(DictOut[key], GPIO.OUT, initial=GPIO.HIGH)



#map buttons to BCM pins per PinOut.md
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) #setup power on indicator light
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setup shutdown btn

comboLookup = {17:[18],27:[23],22:[18,23],5:[25],6:[24]}

#when an input pin is called, toggle the corresponding output pin ON (LOW) and OFF
def thread_outputMacro(pin):
    GPIO.output(comboLookup[pin],GPIO.LOW)
    print "pulling",  "low"
    time.sleep(0.25)
    GPIO.output(comboLookup[pin],GPIO.HIGH)
    print "returning",  "high"

def callback_btnPress(pin):
    #GPIO.output(18, GPIO.LOW)
    if not GPIO.input(pin):
        print "btn %d pressed" % pin
        #t=threading.Thread(target=thread_outputMacro, args=(pin,),name="macroThread")
        #t.start()
        GPIO.output(comboLookup[pin],GPIO.LOW)
    else:
        print "btn %d released" % pin
        GPIO.output(comboLookup[pin], GPIO.HIGH)

# def callback_btnRelease(pin):
#    print "btn %d released" % pin



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
    GPIO.add_event_detect(DictIn[key], GPIO.BOTH, callback=callback_btnPress,bouncetime=100)
    #GPIO.add_event_detect(DictIn[key], GPIO.RISING, callback=callback_btnRelease,bouncetime=300)

GPIO.add_event_detect(16, GPIO.FALLING, callback=callback_btnShutdown, bouncetime=300)

GPIO.output(20,GPIO.HIGH)

try:
    while True:
        time.sleep(1e6)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

