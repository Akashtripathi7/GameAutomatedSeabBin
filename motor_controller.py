import os     #importing os library 
import time   #importing time 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #don't remove this, else you will get an error
import pigpio #importing GPIO library

ESC1=4  #ESC connections with the GPIO pins; note its the BROADCOM number, not the GPIO pin number!
ESC2=17
ESC3=27
ESC4=22

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
pi.set_servo_pulsewidth(ESC4, 0)

max_value = 2000 #change this if your ESC's max value is different or leave it 
min_value = 700  #change this if your ESC's min value is different or leave it 


def start(): 
    time.sleep(1)
    speed = 1100    # change your speed if you want to.... it should be between 700 - 2000
    pi.set_servo_pulsewidth(ESC1, speed)
    pi.set_servo_pulsewidth(ESC2, speed)
    pi.set_servo_pulsewidth(ESC3, speed)
    pi.set_servo_pulsewidth(ESC4, speed)

        

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC1, 0)
    pi.set_servo_pulsewidth(ESC2, 0)
    pi.set_servo_pulsewidth(ESC3, 0)
    pi.set_servo_pulsewidth(ESC4, 0)
    pi.stop()

start()
stop()

