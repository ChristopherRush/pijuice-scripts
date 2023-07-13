from pijuice import PiJuice
import time

# Initialize PiJuice interface
pijuice = PiJuice(1, 0x14)

def check_button_status(button_name, button_data):
    status = button_data[button_name]
    if status['SINGLE_PRESS']:
        print(f"{button_name} button single press")
        pijuice.status.SetButtonEvent(button_name, 'SINGLE_PRESS', False)  # Reset the event
    if status['DOUBLE_PRESS']:
        print(f"{button_name} button double press")
        pijuice.status.SetButtonEvent(button_name, 'DOUBLE_PRESS', False)  # Reset the event
    if status['LONG_PRESS']:
        print(f"{button_name} button long press")
        pijuice.status.SetButtonEvent(button_name, 'LONG_PRESS', False)  # Reset the event

while True:
    # Get the status of the buttons
    button_events = pijuice.status.GetButtonEvents()

    # Check if the 'data' key exists and is a dictionary
    if 'data' in button_events and isinstance(button_events['data'], dict):
        button_data = button_events['data']

        # Check status of each button
        check_button_status('SW1', button_data)
        check_button_status('SW2', button_data)
        check_button_status('SW3', button_data)

    # Delay to prevent CPU overuse
    time.sleep(0.1)
