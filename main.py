#import src.drukomat_class
#import src.program_class
import src.ultrasensor_class
import src.led_class

import time

#drukomat_01 = src.drukomat_class.Drukomat()
#program_01 = src.program_class.Program()

ultrasensor_01 = src.ultrasensor_class.UltraSensor()







host = "imap.gmail.com"
username = "dr.grubylolek@gmail.com"
password = 'lkvd djam lizu exmo'
download_folder = "C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file"





def main():
    
    while True:

        distance = ultrasensor_01.return_value()
        print (distance)
        




main()
