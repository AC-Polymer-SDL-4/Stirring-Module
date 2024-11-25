from machine import Pin, PWM
import time

def initialize_fans(pin_num, frequency = 1000):
    """
    Initialize fan stirring, requires a short period of high PWM to turn on all fans and stir at lower speeds afterwards.
    Arguments:
    ---
    pin_num: the number of the GPIO pin the PCB & fans are connected to
    frequency: the frequency (Hz) for PWM, how quickly the fan switches between power on/off.
    """
    fans_pin = Pin(pin_num, Pin.OUT) #GPIO pin for the fan is connected at pin 0
    fans_pwm = PWM(fans_pin) #initialize PWM at the pin

    fans_pwm.freq(frequency) 
    fans_pwm.duty_u16(65500) 
    time.sleep_ms(60)

    return fans_pwm

def stir(fans_pwm, power, duration):
    """
    Stir using fans at given power(1-100) & duration (in MINUTES)
    0-100 power: minimum 50 to get all fans to spin
    
    Note: use start() before first stir function, however start() is not needed for changing stiring speed afterwards.

    Arguments:
    ---
    power (int): 1-100 (50 required for slow stirring)
    duration (int): duration in MINUTES for stirring
    """
    if power > 0 and power <= 100 and duration > 0:
        dutycycle = power/100*65535
        fans_pwm.duty_u16(int(dutycycle)) #set duty cycle (65535 = 100% power)
        print("duty cycle:", int(dutycycle), "for", duration, "mins")
        time.sleep(int(duration*60)) #stir for duration in minutes
    else:
        print("invalid value for power (0-100) and/or duration(>0)")
        stop(fans_pwm)

def stop(fans_pwm): #to stop stirring
    fans_pwm.duty_u16(0) #duty cycle = 0
    time.sleep_ms(5) #wait for it to stop

try:
    fans = initialize_fans(0) #initialize fans at GPIO pin 0
    stir(fans,60,0.3) #stir at 60% power for 0.3 minute
    stop(fans) #stop stirring

    fans.deinit() #deinitialize the PWM pin
    print("Stirring Complete")


except KeyboardInterrupt:
    print("Program stopped")
    stop(fans)
    fans.deinit()     


