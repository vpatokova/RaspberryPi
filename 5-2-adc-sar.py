import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
max_voltage = 3.3
troyka = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        comparator_value = GPIO.input(comparator)
        if comparator_value == 0:
            value -= 2**i
    return value


try:
    while True:
        value = adc()
        voltage = value / levels * max_voltage

        print("Entered value = {:^3}, output voltage = {:.2f}".format(value, voltage))

except KeyboardInterrupt:
    print("exit")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
