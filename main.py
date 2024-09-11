import time
import RPi.GPIO as GPIO
import src.led_class
import os


"""
import src.drukomat_class
import src.program_class
import src.ultrasensor_class
import src.led_class



drukomat_01 = src.drukomat_class.Drukomat()
program_01 = src.program_class.Program()

ultrasensor_01 = src.ultrasensor_class.UltraSensor()
led_01 = src.led_class.LEDclass()


host = "imap.gmail.com"
username = "dr.grubylolek@gmail.com"
password = 'lkvd djam lizu exmo'
download_folder = "C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file"
"""

led_object = src.led_class.LEDclass()



winda_poziom = int
wolne_boxy = int
zajete_boxy = int

L_box_1 = bool
R_box_1 = bool

def main():
    
    while True:
        os.system("clear")
        
        print("== Podglad ==")
        print(f"Winda poziom: {winda_poziom}")
        print(f"Wolne_boxy: {wolne_boxy}")
        print(f"Zajete boxy: {zajete_boxy}")

        print(f"L_box_1: {L_box_1}")
        print(f"R_box_1{R_box_1}")

        print("=== OPCJE ===")
        print("Print TEST (0)")
        print("Dioda_RED_ON (1)")
        print("Dioda_RED_OFF (2)")

        anser = input("Wybierz opcje: ")

        anser = int 

        if anser == 1:
            led_object.red_led_ON()
            time.sleep(1)
            print ("LED on")
            continue
            

        elif anser == 2:
            led_object.red_led_OFF()
            print("LED off")


        elif anser == 0:
            print("teścik teścik")

        else:
            print("kurcze problem")


    


main()
