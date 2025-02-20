import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Initialize the RFID reader
reader = SimpleMFRC522()

try:
    print("Place your RFID tag to read data.")
    # Read the RFID tag (this will wait until a tag is near)
    id, text = reader.read()
    print(f"Tag ID: {id}")
    print(f"Current Data: {text}")

    print("Now write new data to this tag.")
    # Input data from the user to write to the RFID tag
    data = input("Enter the data to write: ")
    reader.write(data)  # Write the data to the RFID tag
    print("Data written successfully!")

finally:
    GPIO.cleanup()  # Clean up GPIO pins to ensure a clean exit
