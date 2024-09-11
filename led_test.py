import RPi.GPIO as GPIO
import time
import src.led_class


led_class = src.led_class.LEDclass()


def test():

    led_class.red_led_ON()
    time.sleep(1)
    led_class.red_led_OFF()

    led_class.green_led_ON()
    time.sleep(1)
    led_class.green_led_OFF()

    led_class.blue_1_led_ON()
    time.sleep(1)
    led_class.blue_1_led_OFF()

    led_class.blue_2_led_ON()
    time.sleep(1)
    led_class.blue_2_led_OFF


test()