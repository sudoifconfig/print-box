import RPi.GPIO as GPIO
import time




class UltraSensor:
   
    def __init__(self):
      
        GPIO.setmode(GPIO.BOARD)
        

        self.trig = 18
        self.echo = 16
        self.i = 1
        
        GPIO.output(self.trig, False)
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)

        



    def return_value(self):

        try:

            GPIO.output(self.trig, False)
            print ("Calibrating.....")
            time.sleep(2)

            GPIO.output(self.trig, True)
            time.sleep(0.00001)
            GPIO.output(self.trig, False)

            while GPIO.input(self.echo)==0:
                pulse_start = time.time()

            while GPIO.input(self.echo)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150

            distance = round(distance+1.15, 2)

            return distance
        
        except:
            print("Problem")