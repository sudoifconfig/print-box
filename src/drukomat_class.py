import RPi.GPIO as GPIO




class Drukomat:

    def __init__(self):
        
        self.wolne_skrzynki = [1,2,3]
        self.zajete_skrzynki = []

        self.sensor_value = float



    def winda_na_x_pietro_od_1_do_3(self,x):
        
        if x == 1:
            
            while self.return_sensor_value() < 10:
                GPIO.pin14.ON
                
            self.podajnik_tasmowy(self)


        if x == 2:
            
            while self.return_sensor_value() < 20:
                GPIO.pin14.ON
                
            self.podajnik_tasmowy(self)

        if x == 3:
            while self.return_sensor_value() < 30:
                GPIO.pin14.ON
                
            self.podajnik_tasmowy(self)

        else:
            print ("ERROR, nie prawidłowa wartość [class drukomat func. winda_na_x_pietro()]")





    def podajnik_tasmowy(self):
        # Na np 5 sekund
        GPIO.pin25.ON

    def return_sensor_value(self):
        # tutaj kodzik dla sensora odległości
        pass 


    def print_test(self):
        print("TEST class Drukomat print")