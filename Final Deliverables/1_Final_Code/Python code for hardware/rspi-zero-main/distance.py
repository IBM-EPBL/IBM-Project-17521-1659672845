import RPi.GPIO as GPIO
import time

  
def distancesensor():
  try:

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        PIN_TRIGGER = 23
        PIN_ECHO = 33
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

  
        time.sleep(2)
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
  
        time.sleep(0.00001)
  
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
  
        while GPIO.input(PIN_ECHO)==0:
              pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
              pulse_end_time = time.time()
  
        pulse_duration = pulse_end_time - pulse_start_time
        global distance
        distance = round(pulse_duration * 17150, 2)
        print(distance)
        return distance


  finally:
      GPIO.cleanup()


