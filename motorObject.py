import RPi.GPIO as GPIO
import time
from threading import *
class motor(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.numPeople = 0
        in1 = 4
        in2 = 17
        in3 = 23
        in4 = 24
         
        # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
        self.step_count = 514
         
        direction = False # True for clockwise, False for counter-clockwise

        personHere = False
         

         
        # setting up
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( in1, GPIO.OUT )
        GPIO.setup( in2, GPIO.OUT )
        GPIO.setup( in3, GPIO.OUT )
        GPIO.setup( in4, GPIO.OUT )
         
        # initializing
        GPIO.output( in1, GPIO.LOW )
        GPIO.output( in2, GPIO.LOW )
        GPIO.output( in3, GPIO.LOW )
        GPIO.output( in4, GPIO.LOW )
         
        GPIO.setwarnings(False)
         
        self.motor_pins = [in1,in2,in3,in4]
        motor_step_counter = 0 


    def getNumPeople(self):
        return self.numPeople

    def setNumPeople(self,numPeople):
        self.numPeople = numPeople

    def cleanup(self):
        in1 = 4
        in2 = 17
        in3 = 23
        in4 = 24
        GPIO.output( in1, GPIO.LOW )
        GPIO.output( in2, GPIO.LOW )
        GPIO.output( in3, GPIO.LOW )
        GPIO.output( in4, GPIO.LOW )

    def oneDirection(self, motor_step_counter, direction):
        step_sleep = 0.05

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        step_sequence = [[1,0,0,1],
                         [1,0,0,0],
                         [1,1,0,0],
                         [0,1,0,0],
                         [0,1,1,0],
                         [0,0,1,0],
                         [0,0,1,1],
                         [0,0,0,1]]
        for i in range(self.step_count):
                for pin in range(0, len(self.motor_pins)):
                    GPIO.output(self.motor_pins[pin], step_sequence[motor_step_counter][pin] )
                if direction==True:
                    motor_step_counter = (motor_step_counter - 1) % 8
                elif direction==False:
                    motor_step_counter = (motor_step_counter + 1) % 8
                else: # defensive programming
                    print( "uh oh... direction should *always* be either True or False" )
                    cleanup()
                    exit( 1 )
                time.sleep( step_sleep )
                    
    def camMove(self,motor_step_counter,NumPeopleFunction):
        while True:
            NumPeople = NumPeopleFunction()
            print("in the MOTOR CODE" , NumPeople)
            if NumPeople == 0:
                self.oneDirection(motor_step_counter,False)
                self.oneDirection(motor_step_counter, True)
            else:
                print("I FOUYND YOU BITTTTTCHHHHHHH")
                self.cleanup()
            

    
    
