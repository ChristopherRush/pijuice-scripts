from pijuice import PiJuice
import time

# Initialize PiJuice interface
pijuice = PiJuice(1, 0x14)

def check_button_status(button_events, button_name):
    if button_events['error'] != 'NO_ERROR':
        print("Error in getting button status")
        return

    status = button_events['data'][button_name]

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

    # Check status of each button
    check_button_status(button_events, 'SW1')
    check_button_status(button_events, 'SW2')
    check_button_status(button_events, 'SW3')

    # Delay to prevent CPU overuse
    time.sleep(0.1)
