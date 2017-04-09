import RPi.GPIO as GPIO
import time
import threading
import os
GPIO.setmode(GPIO.BCM) #use BCM numbering scheme

#threadList = []


DictIn = {1:17,2:27,3:22,4:5,5:6,6:26}
DictOut = {'A':18,'B':23,'C':25,'Z':24}
WII_A = 18
WII_B = 23
WII_C = 25
WII_Z = 24

for key in DictIn:
    GPIO.setup(DictIn[key], GPIO.IN, pull_up_down=GPIO.PUD_UP)

for key in DictOut:
    GPIO.setup(DictOut[key], GPIO.OUT, initial=GPIO.HIGH)



#map buttons to BCM pins per PinOut.md
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) #setup power on indicator light
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setup shutdown btn

comboLookup = {17:[0,WII_A], 27:[1,WII_A, 0.250, WII_A, 0.250, WII_B, 0.250],22:[0, WII_Z],5:[0, WII_A, WII_B],6:[0, WII_C]}

#when an input pin is called, toggle the corresponding output pin ON (LOW) and OFF
def thread_seqMacro(pin):
    for i in range(1, len(comboLookup[pin]), 2): #iterate through the list of btns, starting from 1, skipping over the durations
        GPIO.output(comboLookup[pin][i],GPIO.LOW)
        print "pulling",  "low"
        dur = comboLookup[pin][i+1]
        time.sleep(dur)
        GPIO.output(comboLookup[pin][i],GPIO.HIGH)
        print "returning",  "high"
        time.sleep(0.1)

def callback_btnPress(pin):
    #GPIO.output(18, GPIO.LOW)
    if not GPIO.input(pin):
        print "btn %d pressed" % pin
        if comboLookup[pin][0]==0:
            GPIO.output(comboLookup[pin][1:],GPIO.LOW)
        elif comboLookup[pin][0]==1:
            t=threading.Thread(target=thread_seqMacro, args=(pin,),name="macroThread")
            t.start()
#            if threadList
#                lastCombo=threadList.pop()
#                lastCombo
#            threadList.appedn(t)
    else:
        print "btn %d released" % pin
        if comboLookup[pin][0]==0:
            GPIO.output(comboLookup[pin][1:], GPIO.HIGH)
        # elif comboLookup[pin][0]==1:s

# def callback_btnRelease(pin):
#    print "btn %d released" % pin



def callback_btnShutdown(pin):
    time.sleep(2)
    if not GPIO.input(pin):
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

