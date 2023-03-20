import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(2, GPIO.OUT)

pwm = GPIO.PWM(2, 1000)
pwm.start(0)
try:
    while True:
        duty_cycle = int(input())
        pwm.ChangeDutyCycle(duty_cycle)
        print("{:.2f}".format(duty_cycle*3.3/100))
    
except KeyboardInterrupt:
    print("цикл завершен")
finally:
    GPIO.output(dac, 0)
    GPIO.output(2, 0)
    GPIO.cleanup() 
