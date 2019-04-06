import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinNum = 17
GPIO.setup(pinNum,GPIO.OUT)


if GPIO.input(pinNum) == LOW:
     print("lights on!")
     GPIO.output(pinNum, GPIO.HIGH)
elif GPIO.input(pinNum) == HIGH:
     print("lights off!")
     GPIO.output(pinNum, GPIO.LOW)
else:
    print("error")
