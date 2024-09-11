import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module



class LEDclass:
    
    def __init__(self):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # RED
        GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # GREEN
        GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # BLUE1
        GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #BLUE2

        GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # PRINTER
        GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # TRANSPORT_BANDA
        GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # TRANSPORT_BANDA

        



    
    def red_led_ON(self):

        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
        

    def red_led_OFF(self):
        GPIO.output(8, GPIO.LOW)



    def green_led_ON(self):
        GPIO.output(10, GPIO.HIGH)


    def green_led_OFF(self):
        GPIO.output(10, GPIO.LOW)



    
    def blue_1_led_ON(self):
        GPIO.output(12, GPIO.HIGH)

    def blue_1_led_OFF(self):
        GPIO.output(12, GPIO.LOW)


    def blue_2_led_ON(self):
        GPIO.output(16, GPIO.HIGH)

    def blue_2_led_OFF(self):
        GPIO.output(16, GPIO.LOW)