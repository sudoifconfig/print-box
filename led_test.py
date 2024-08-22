import RPi.GPIO as GPIO
import time
import src.led_class

"""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(8,GPIO.LOW)"""


led_01 = src.led_class.LEDclass()


led_01.red_led_ON