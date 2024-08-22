import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module



class LEDclass:
    
    def __init__(self):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial va>
        GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and s>
        GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and s>

    
    def red_led_ON(self):

        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
        

    def red_led_OFF(self):
        GPIO.output(8, GPIO.LOW)



    def green_led_ON(self):
        GPIO.output(10, GPIO.HIGH)


    def green_led_OFF(self):
        GPIO.output(10, GPIO.LOW)



    
    def yelow_led_ON(self):
        GPIO.output(12, GPIO.HIGH)

    def yelow_led_OFF(self):
        GPIO.output(12, GPIO.LOW)