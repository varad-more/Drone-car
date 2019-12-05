import tty
import sys
import termios
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

orig_settings = termios.tcgetattr(sys.stdin)

tty.setcbreak(sys.stdin)

Motor1R = 35    # Input Pin
Motor1L = 36    # Input Pin
Motor2R = 37    # Input Pin
Motor2L = 38    # Input Pin


GPIO.setup(Motor1R,GPIO.OUT)
GPIO.setup(Motor1L,GPIO.OUT)
GPIO.setup(Motor2R,GPIO.OUT)
GPIO.setup(Motor2L,GPIO.OUT)


GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)




# 12 & 15 -- White Wings CCR
# 11 & 13 -- Red Wings CR

"""
Front --- Span between 11 & 12
Wider gap & camera holding
"""
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
y1=y2=y3=y4=6.0
x = 0
mode=0
while x != chr(27): # ESC

    while (mode==1):
        l=r=up=dn=fd=bk=0.0

        x=sys.stdin.read(1)[0]
        if x=="a":
            print ("Left")
            l=0.1
        elif x=="d":
            print ("Right")
            r=0.1
        elif x=="s":
            print ("BACK")
            bk=0.1
        elif x=="w":
            print ("FORWARD")
            fk=0.1
        elif x=="i":
            print ("Throttle Inc")
            up=0.1
        elif x=="k":
            print ("Throttle Dec")
            dn=0.1
        elif x =="b":
            mode=0
            print ("Mode Changed to Car")
        else:
            print ("Invalid")

        y1=y1+up-dn-fd+bk+r-l
        y2=y2+up-dn-fd+bk-r+l
        y3=y3+up-dn+fd-bk-r+l
        y4=y4+up-dn+fd-bk+r-l
        print (y1,"\t"+ y2,"\t" + y3,"\t" + y4 )
        t1.ChangeDutyCycle(y1)
        t2.ChangeDutyCycle(y2)
        t3.ChangeDutyCycle(y3)
        t4.ChangeDutyCycle(y4)
    #print (y+up-dn)
  #  print("You pressed", x)



    while (mode==0):
        
        if x=="a":
            print ("Left")
            GPIO.output(Motor1R,GPIO.LOW)
            GPIO.output(Motor1L,GPIO.LOW)
            GPIO.output(Motor2R,GPIO.HIGH)
            GPIO.output(Motor2L,GPIO.HIGH)
        elif x=="d":
            print ("Right")
            GPIO.output(Motor1R,GPIO.HIGH)
            GPIO.output(Motor1L,GPIO.HIGH)
            GPIO.output(Motor2R,GPIO.LOW)
            GPIO.output(Motor2L,GPIO.LOW)
        elif x=="s":
            print ("BACK")
            GPIO.output(Motor1R,GPIO.LOW)
            GPIO.output(Motor1L,GPIO.HIGH)
            GPIO.output(Motor2R,GPIO.LOW)
            GPIO.output(Motor2L,GPIO.HIGH)

        elif x=="w":
            print ("FORWARD")
            GPIO.output(Motor1R,GPIO.HIGH)
            GPIO.output(Motor1L,GPIO.LOW)  
            GPIO.output(Motor2R,GPIO.HIGH)
            GPIO.output(Motor2L,GPIO.LOW)  

        elif x =="b":
            mode=1
            print ("Mode Changed to Drone")
        else:
            print ("Invalid")


termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    

t1.stop()
t2.stop()
t3.stop()
t4.stop()

GPIO.cleanup()
quit()
