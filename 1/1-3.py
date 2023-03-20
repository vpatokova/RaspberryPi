import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(2, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

GPIO.output(2, GPIO.input(15))
