import src.drukomat_class
import src.program_class
import src.ultrasensor_class
import src.led_class

import time

drukomat_01 = src.drukomat_class.Drukomat()
program_01 = src.program_class.Program()

ultrasensor_01 = src.ultrasensor_class.UltraSensor()
led_01 = src.led_class.LEDclass()


host = "imap.gmail.com"
username = "dr.grubylolek@gmail.com"
password = 'lkvd djam lizu exmo'
download_folder = "C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file"



def main():
    
    while True:

        print("Print TEST (0)")
        print("Drukuj plik PDF (1)")
        print("Winda na poziom X (2)")
        print("Przechyl w LEWO (3)")
        print("Przechyl w PRAWO (4)")
        print("Zapadka_1 ON poziom 1 (5)")

        anser = input("Wybierz opcje: ")

        anser = int 

        if anser == 1:
            pass

        if anser == 2:
            pass

        if anser == 0:
            print("teścik teścik")



    


main()
