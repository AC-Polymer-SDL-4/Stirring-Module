from machine import Pin, PWM
import time

class StirringModule:
    PIN_NUM = 0 #GPIO pin number the fans are connected to
    fans_pwm = ""
    initialized = False #tracks if fans have been "initialized" (need to stir at high power for 60ms to turn all fans on before stirring)
    led = None

    def __init__(self, frequency = 1000) -> None:
        """
        Initialize StirringModule for stirring.
        
        Parameters:
        ---
        frequency: the frequency (Hz) for PWM, how quickly the fan switches between power on/off.

        """
        try:
            self.fans_pin = Pin(self.PIN_NUM, Pin.OUT)
            self.fans_pwm = PWM(self.fans_pin) #initialize PWM at the pin

            self.fans_pwm.freq(frequency) #set frequency
            
            self.led = Pin("LED", Pin.OUT) #on-board led light
            
            print("Stirring Module initializated")
        
        except Exception as e:
            print("Could not initialize stirring module: ", e)
            self.stop()

        

    def initialize_fans(self):
        """The fans require a short period of high PWM to turn on all fans and stir at lower speeds afterwards. This should be used before stirring."""
        self.fans_pwm.duty_u16(65500) #turn on max PWM for 60 milliseconds.
        time.sleep_ms(60)
        self.initialized = True

    def stir_for_duration(self, power, duration):
        """
        Stir using fans at given power(1-100) & duration (in MINUTES) and then stops.

        Parameters:
        ---
        power (int): 1-100 (minimum 45 for all fans to turn on)
        duration (float): stirring duration in MINUTES
        """
        if self.initialized == False:
            self.initialize_fans()
            
        self.led.value(1) #turn on light 

        if power > 0 and power <= 100 and duration > 0:
            dutycycle = power/100*65535
            self.fans_pwm.duty_u16(int(dutycycle)) #set duty cycle (65535 = 100% power)
            print(f"Stirring at {power}% power for {duration} minutes")
            time.sleep(int(duration*60)) #stir for duration in minutes
            self.stop()
            return True
        else:
            print("Invalid value for power (0-100) and/or duration(>0)")
            self.stop()
            return False

    def stir(self,power):
        """
        Stir using fans at given power(1-100) until stopped using the stop() function

        Parameters:
        ---
        power (int): 1-100 (minimum 45 for all fans to turn on)
        """
        if self.initialized == False:
            self.initialize_fans()
        
        self.led.value(1) #turn on light 
        
        if power > 0 and power <= 100:
            dutycycle = power/100*65535
            self.fans_pwm.duty_u16(int(dutycycle)) #set duty cycle (65535 = 100% power)
            print(f"Stirring at {power}% power until stopped")
            return True
        else:
            print("ERROR: Invalid value for power (1-100)")
            self.stop()
            return False

    def stop(self): #to stop stirring
        """
        Stops fans from stirring & deinitializes pin from signal
        """
        
        self.led.value(0) #turn off light
        
        self.fans_pwm.duty_u16(0) #duty cycle = 0
        time.sleep_ms(5) #wait for it to stop
        self.fans_pwm.deinit()
        self.initialized = False
        print("Fans stopped and deinitialized")

# General methods -- to be called using controller
def initialize_and_stir(power, duration):
    """Initializes fans, stirs for designated amount of time at specified power and de-initializes fans at the end.
    
    Parameters:
    ---
    power(int): 1-100, for controlling stirring speed (minimum 45 to turn on all fans)
    duration (float): stirring duration in MINUTES
    """
    s = StirringModule()
    status = s.stir_for_duration(power=power, duration=duration)
    if status:
        print(f"Fan stirring at {power}% power for {duration} minutes complete")
    else:
        print("Invalid input for stirring")

def controller_stir(power):
    s = StirringModule()
    s.stir(power)

def controller_stop():
    s = StirringModule()
    s.stop()
    
#controller_stir(60)
#time.sleep(5)
#controller_stop()

