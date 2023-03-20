import RPi.GPIO as GPIO
import time


def mezure_potential(num, dac):
    number = []
    k = 0
    while num > 0:
        number.append(num % 2)
        num //= 2
        k += 1
    for i in range(8-k):
        number.append(0)
     
    number = list(reversed(number))

    GPIO.output(dac, number)
    time.sleep(15)
    GPIO.output(dac, 0)

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

number = [255, 127, 64, 32, 5, 0, 253]

GPIO.setup(dac, GPIO.OUT)

for num in number:
    mezure_potential(num, dac)

GPIO.cleanup()
