import time
import board
import digitalio
import pulseio
from adafruit_motor import servo

# Built in red LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, frequency=50)

# Create a servo object, which actually controls a brushless motor.
brushless = servo.Servo(pwm,min_pulse=1000,max_pulse=2000)

while True:
    # first, go into an arming period during which you can connect the battery to the ESC
    brushless.angle=0
    led.value = 1 # turn on red LED to let us know we're in the arming period.
    time.sleep(5)


    # now set speed to 20%
    brushless.angle=36
    time.sleep(5)

     # now set speed to 30%
    brushless.angle=54
    time.sleep(5)

     # now set speed to 40%
    brushless.angle=72
    time.sleep(5)

    # now set speed to 50%
    brushless.angle=90
    time.sleep(5)

    # now set speed to 100%
    brushless.angle=180
    time.sleep(5)