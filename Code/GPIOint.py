import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)

DictIn = {1:17,2:27,3:22,4:5,5:6}

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) #setup power button

comboLookup = {17:[18],27:[23],22:[18,23]}

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

GPIO.add_event_detect(27, GPIO.FALLING, callback=callback_btnPress,bouncetime=500)
GPIO.add_event_detect(17, GPIO.FALLING, callback=callback_btnPress,bouncetime=500)
GPIO.add_event_detect(22, GPIO.FALLING, callback=callback_btnPress,bouncetime=500)

GPIO.output(21,GPIO.HIGH)

try:
    while True:
        time.sleep(1e6)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
