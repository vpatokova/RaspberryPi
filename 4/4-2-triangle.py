import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        p = input()
        if not p.isdigit():
            print("not a number")
        else:
            period = int(p)/256/2
            for i in range(256):
                GPIO.output(dac, dec2bin(i))
                time.sleep(period)
            for i in range(255, -1, -1):
                GPIO.output(dac, dec2bin(i))
                time.sleep(period)
except KeyboardInterrupt:
    print("цикл завершен")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
