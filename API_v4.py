import requests
import webbrowser
import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from create_html_file_v3 import create_html_file

# Your Sketchfab API key
api_key = "1a53843034804dfda647a3a20523b479"
reader = SimpleMFRC522()
tag_id_list = [534080257907,839939270962,632472152511,417427926619]


def read_rfid_data():
    try:
        print("Place your RFID tag to read data.")
        id, text = reader.read()
        print(f"Tag ID: {id}")
        print(f"Current Data: {text}")
    finally:
        GPIO.cleanup()  # Clean up GPIO pins to ensure a clean exit
    return id,str(text)  # Remove any extra spaces or characters

def open_html_in_browser(html_file):
    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{os.path.realpath(html_file)}")


# Main Program
data = read_rfid_data()
if data[0] in tag_id_list:
    print(f"ID from RFID: {data[0]}")
    # Create the HTML file with the embed code inserted
    html_file = create_html_file()

    # Automatically open the generated HTML file in the web browser
    open_html_in_browser(html_file)
else:
    print("Not valid ID found from RFID tag.")
