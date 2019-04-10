import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinNum = 17
GPIO.setup(pinNum,GPIO.OUT)

GPIO.output(pinNum, GPIO.LOW)
