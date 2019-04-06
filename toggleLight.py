import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinNum = 17
GPIO.setup(pinNum,GPIO.OUT)


if GPIO.output(pinNum) == LOW:
     print("lights on!")
     GPIO.output(pinNum, GPIO.HIGH)
elif GPIO.output(pinNum) == HIGH:
     print("lights off!")
     GPIO.output(pinNum, GPIO.LOW)
else:
    print("error")
