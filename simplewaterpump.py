import RPi.GPIO as GPIO
import datetime
import time
import os.path
import csv



GPIO.setmode(GPIO.BCM) # 

# store pump BCM pins
pump_pin=24



# this is a test
def runtest():
    
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)

    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(24, True)
    time.sleep(5)
    print ("LED off")
    GPIO.output(18,GPIO.LOW)
    GPIO.output(24, False)
    GPIO.cleanup()



# initial pump pin
def init_pump(pump_pin):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setwarnings(False)
    GPIO.setup(pump_pin, GPIO.OUT)
    print('pump pin {} init'.format (pump_pin))
    
    
    
# turn on pump     
def pump_on(pump_pin, delay):
    
    start_time=time.time()
    act='pump pin {}'.format(pump_pin)
    notes=''
   
    init_pump(pump_pin)
    
#     f = open("pump_on.txt", "a")
#     f.write("Turn on pump at {} ".format(datetime.datetime.now()))
#     f.write('\n')
#     f.close()
    #GPIO.setmode(GPIO.BCM)
    GPIO.setup(pump_pin, GPIO.OUT)
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pump_pin, GPIO.HIGH)
    cleanup_pump_pin()
    end_time=time.time()-start_time
    
    write_log(start_time, act, end_time, notes)
          
  
  
def get_status(pump_pin):
    GPIO.setmode(GPIO.BCM) #
    GPIO.setup(pump_pin, GPIO.IN)
    GPIO.cleanup()
    return GPIO.input(pump_pin)
