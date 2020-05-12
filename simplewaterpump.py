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



def cleanup_pump_pin():
    GPIO.cleanup()



# write data log to csv file in the same folder
def write_log(st, act, et, notes):
    '''
    write_log (start time, activity, end time , notes)

    '''
    filename='waterlog.csv'
    file_exists = os.path.isfile(filename)
    
    header = ['Epoch', 'Activity', 'RunTime', 'Notes']
    
    rows = [[st, act, et, notes]]
    
    with open(filename, 'a') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        if not file_exists:
            csv_writer.writerow(header) # write header
        
        csv_writer.writerows(rows)


# run pump_on function
pump_on(pump_pin, 2)
