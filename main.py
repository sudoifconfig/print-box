import time
import RPi.GPIO as GPIO
import src.led_class



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
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_object = src.led_class.LEDclass()



winda_poziom = int
wolne_boxy = int
zajete_boxy = int

L_box_1 = bool
R_box_1 = bool

def main():
    
    while True:

        print("==Podglad==")
        print(f"Winda poziom: {winda_poziom}")
        print(f"Wolne_boxy: {wolne_boxy}")
        print(f"Zajete boxy: {zajete_boxy}")

        print(f"L_box_1: {L_box_1}")
        print(f"R_box_1{R_box_1}")


        print("Print TEST (0)")
        print("Dioda_RED_ON (1)")
        print("Dioda_RED_OFF (2)")

        anser = input("Wybierz opcje: ")

        anser = int 

        if anser == 1:
            led_object.red_led_ON()
            print ("LED on")
            

        if anser == 2:
            led_object.red_led_OFF()
            print("LED off")


        if anser == 0:
            print("teścik teścik")



    


main()
