import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

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

t1.ChangeDutyCycle(4.5)
t2.ChangeDutyCycle(4.5)
t3.ChangeDutyCycle(4.5)
t4.ChangeDutyCycle(4.5)



time.sleep(3)
#x=6
#y=6
x=6.5
#while (x<6.1):
t1.ChangeDutyCycle(x)
t2.ChangeDutyCycle(x)
t3.ChangeDutyCycle(x)
t4.ChangeDutyCycle(x)
#x=x+0.1
#time.sleep(3)

time.sleep(6)


t1.stop()
t2.stop()
t3.stop()
t4.stop()




GPIO.cleanup()
quit()
