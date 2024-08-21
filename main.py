#import src.drukomat_class
#import src.program_class
import src.ultrasensor_class
import src.led_class
i

import time

#drukomat_01 = src.drukomat_class.Drukomat()
#program_01 = src.program_class.Program()

ultrasensor_01 = src.ultrasensor_class.UltraSensor()
led_01 = src.led_class.LEDclass()


host = "imap.gmail.com"
username = "dr.grubylolek@gmail.com"
password = 'lkvd djam lizu exmo'
download_folder = "C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file"



def main():
    
    while True:

        distance = ultrasensor_01.return_value()
        print (distance)

        if distance <= 10.00:
            led_01.red_led_ON

        if distance > 10.00:
            led_01.yelow_led_ON

        if distance > 20.00:
            led_01.green_led_ON

        time.sleep(0.2)








        




main()
