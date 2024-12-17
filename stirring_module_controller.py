import subprocess

def run_stirring_module(pin_num, power, duration):
    """
    Initializes fans and stirs. Currently set to GPIO pin 0 (in stirring_module.py)
    Parameters
    ---
    power: 1-100, the stirring speed (minimum 45 for all fans to spin)
    duration: number of minutes to stir for
    """
    try:
        # Run the mpremote command as a subprocess
        command = f"import stirring_module; stirring_module.initialize_and_stir({pin_num},{power},{duration})" 
        result = subprocess.run(
            ['mpremote', 'connect', 'COM11', 'exec', command], #may need to edit COM number for your computer
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

#running the method
run_stirring_module(pin_num = 0, power=60, duration=.15) #edit values as desired