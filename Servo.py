import board
import time
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm,min_pulse=500,max_pulse=2400)

while True:
    for angle in range(0, 180, 90): # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)
    for angle in range(180, 90, -90): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.5)
    for angle in range(90, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.5)
