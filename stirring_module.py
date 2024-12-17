from machine import Pin, PWM
import time

PIN_NUM = 0 #EDIT THIS for the GPIO pin you have the fans connected to

def initialize_fans(frequency = 1000):
    """
    Initialize fan stirring, requires a short period of high PWM to turn on all fans and stir at lower speeds afterwards.
    
    Parameters:
    ---
    frequency: the frequency (Hz) for PWM, how quickly the fan switches between power on/off.

    Returns:
    ---
    PWM object at the designated GPIO pin
    """
    fans_pin = Pin(PIN_NUM, Pin.OUT) #GPIO pin for the fan is connected at pin 0
    fans_pwm = PWM(fans_pin) #initialize PWM at the pin

    fans_pwm.freq(frequency) #set frequency 
    fans_pwm.duty_u16(65500) #turn on max PWM for 60 milliseconds.
    time.sleep_ms(60)

    return fans_pwm

def stir(fans_pwm, power, duration):
    """
    Stir using fans at given power(1-100) & duration (in MINUTES)
    Note: use start() before your first stir function. start() is not needed for changing stirring speed afterwards.

    Parameters:
    ---
    power (int): 1-100 (50 required for all fans to turn on)
    duration (float): stirring duration in MINUTES
    """
    if power > 0 and power <= 100 and duration > 0:
        dutycycle = power/100*65535
        fans_pwm.duty_u16(int(dutycycle)) #set duty cycle (65535 = 100% power)
        print(f"Stirring at {power} % power (duty cycle: {int(dutycycle)}) for {duration} minutes")
        time.sleep(int(duration*60)) #stir for duration in minutes
    else:
        print("invalid value for power (0-100) and/or duration(>0)")
        stop(fans_pwm)

def stop(fans_pwm): #to stop stirring
    fans_pwm.duty_u16(0) #duty cycle = 0
    time.sleep_ms(5) #wait for it to stop

def initialize_and_stir(duration, power):
    """Initializes fans, stirs for designated amount of time at specified power and de-initializes fans at the end.
    
    Parameters:
    ---
    duration (float): stirring duration in MINUTES
    power(int): 0-100, for controlling stirring speed (minimum 50 to turn on all fans)
    """
    fans = initialize_fans()
    stir(fans, duration=duration, power=power)
    stop(fans)
    fans.deinit()
    print("Fan initialization & stirring complete")   


