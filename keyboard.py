import tty
import sys
import termios

orig_settings = termios.tcgetattr(sys.stdin)

tty.setcbreak(sys.stdin)
x = 0
while x != chr(27): # ESC
    x=sys.stdin.read(1)[0]
    if x=="a":
        print ("Left")
    elif x=="d":
        print ("Right")
    elif x=="s":
        print ("Down")
    elif x=="w":
        print ("Up")
    elif x=="i":
        print ("Throttle Inc")
    elif x=="k":
        print ("Throttle Dec")
    else:
        print ("Invalid")


  #  print("You pressed", x)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    