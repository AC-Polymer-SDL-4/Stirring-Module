from machine import Pin, PWM
import time

def initialize_fans(pin_num, frequency = 1000):
    """
    Initialize fan stirring, requires a short period of high PWM to turn on all fans and stir at lower speeds afterwards.
    
    Parameters:
    ---
    pin_num: the GPIO pin number the fans are connected to
    frequency: the frequency (Hz) for PWM, how quickly the fan switches between power on/off.

    Returns:
    ---
    PWM object at the designated GPIO pin
    """
    fans_pin = Pin(pin_num, Pin.OUT) #GPIO pin for the fan is connected at pin 0
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
    power (int): 1-100 (minimum 45 for all fans to turn on)
    duration (float): stirring duration in MINUTES
    """
    if power > 0 and power <= 100 and duration > 0:
        dutycycle = power/100*65535
        fans_pwm.duty_u16(int(dutycycle)) #set duty cycle (65535 = 100% power)
        print(f"Stirring at {power} % power for {duration} minutes")
        time.sleep(int(duration*60)) #stir for duration in minutes
    else:
        print("invalid value for power (0-100) and/or duration(>0)")
        stop(fans_pwm)

def stop(fans_pwm): #to stop stirring
    fans_pwm.duty_u16(0) #duty cycle = 0
    time.sleep_ms(5) #wait for it to stop

def initialize_and_stir(pin_num, power, duration):
    """Initializes fans, stirs for designated amount of time at specified power and de-initializes fans at the end.
    
    Parameters:
    ---
    power(int): 1-100, for controlling stirring speed (minimum 45 to turn on all fans)
    duration (float): stirring duration in MINUTES
    """
    fans = initialize_fans(pin_num)
    stir(fans, power=power, duration=duration)
    stop(fans)
    fans.deinit()
    print("Fan initialization & stirring complete")   

#Uncomment the following lines if you are uploading the file to the RPi and running it through REPL
# try:
#     fans = initialize_fans(0) #initialize fans at GPIO pin 0
#     stir(fans, power=60, duration=0.2) #edit power & duration values as desired
#     stop(fans) #stop fans
#     fans.deinit() #deinitialize PWM pin
#     print("Stirring Complete")

# except KeyboardInterrupt: #stops fans when ctrl+c is pressed
#     stop(fans) 
#     fans.deinit()
#     print("Stirring stopped")