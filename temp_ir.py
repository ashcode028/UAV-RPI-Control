import RPi.GPIO as GPIO
import time

sensor = 16
buzzer = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print("IR Sensor Ready.....")


try: 
   while True:
      if GPIO.input(sensor):
          time1 = time.time()
          GPIO.output(buzzer,True)
          time2= time.time()
          print("Object Detected in "+str(time2-time1))
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()

