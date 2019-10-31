import tty
import sys
import termios
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

orig_settings = termios.tcgetattr(sys.stdin)

tty.setcbreak(sys.stdin)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


t1 = GPIO.PWM(11, 50)
t2 = GPIO.PWM(12, 50)
t3 = GPIO.PWM(13, 50)
t4= GPIO.PWM(15, 50)


t1.start(0)
t2.start(0)
t3.start(0)
t4.start(0)

#Initial Write
t1.ChangeDutyCycle(4.5)
t2.ChangeDutyCycle(4.5)
t3.ChangeDutyCycle(4.5)
t4.ChangeDutyCycle(4.5)



time.sleep(3)
y=6.0
x = 0

while x != chr(27): # ESC
    l=r=up=dn=f=b=0.0

    x=sys.stdin.read(1)[0]
    if x=="a":
        print ("Left")
        l=0.1
    elif x=="d":
        print ("Right")
        r=0.1
    elif x=="s":
        print ("back")
        b=0.1
    elif x=="w":
        print ("Front")
        f=0.1    
    elif x=="i":
        print ("Throttle Inc")
        up=0.2
    elif x=="k":
        print ("Throttle Dec")
        dn=0.1
    else:
        print ("Invalid")

    y=y+up-dn
    print (y)
    t1.ChangeDutyCycle(y)
    t2.ChangeDutyCycle(y)
    t3.ChangeDutyCycle(y)
    t4.ChangeDutyCycle(y)
    #print (y+up-dn)
  #  print("You pressed", x)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    

t1.stop()
t2.stop()
t3.stop()
t4.stop()

GPIO.cleanup()
quit()
