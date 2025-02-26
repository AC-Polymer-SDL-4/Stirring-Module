import subprocess
import time

def run_command(command):
    try:
        result = subprocess.run(
            ['mpremote', 'connect', 'COM3', 'exec', command], #edit com port number
            stdout=subprocess.PIPE,  # Capture the output of the command
            stderr=subprocess.PIPE,  # Capture any error output
            text=True  # Ensure the output is returned as a string
        )

        # Print the output and error (if any)
        print("Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"Error running mpremote: {e}")

def start_stirring(power):
    """
    Initializes fans and stirs until the stop() command.
    Parameters
    ---
    power: 1-100, the stirring speed (minimum 45 for all fans to spin)
    """
    command = f"import stirring_module; stirring_module.controller_stir({power})" 
    run_command(command)

def stop_stirring():
    """
    Stops stirring.
    """
    command = f"import stirring_module; stirring_module.controller_stop()" 
    run_command(command)

def stir_for_duration(power, duration):
    """
    Initializes fans and stirs for the designated amount of time in minutes.
    Parameters
    ---
    power: 1-100, the stirring speed (minimum 45 for all fans to spin)
    duration: time in MINUTES
    """
    command = f"import stirring_module; stirring_module.initialize_and_stir({power},{duration})" 
    run_command(command)


#running the methods
# start_stirring(power=50) #edit values as desired
# time.sleep(60)
# stop_stirring()
#stir_for_duration(60, 0.2)