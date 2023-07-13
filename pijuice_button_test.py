from pijuice import PiJuice

# Initialize PiJuice interface
pijuice = PiJuice(1, 0x14)

while True:
    # Get the status of the buttons
    button_status = pijuice.status.GetButtonStatus()

    # Function to check button status
    def check_button_status(button_name):
        status = button_status['data'][button_name]
        if status == 'SINGLE_PRESS':
            print(f"{button_name} button single press")
        elif status == 'DOUBLE_PRESS':
            print(f"{button_name} button double press")
        elif status == 'LONG_PRESS':
            print(f"{button_name} button long press")
        else:
            print(f"{button_name} button is not pressed")

    # Check status of each button
    check_button_status('SW1')
    check_button_status('SW2')
    check_button_status('SW3')

    # Delay to prevent CPU overuse
    time.sleep(0.1)
