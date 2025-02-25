import requests
import webbrowser
import os
from create_html_file_v3 import create_html_file


# Your Sketchfab API key
api_key = "1a53843034804dfda647a3a20523b479"
tag_id_list = [534080257907,839939270962,632472152511,417427926619]
tag_id = 534080257907


def open_html_in_browser(html_file):
    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{os.path.realpath(html_file)}")


# Main Program
# Create the HTML file with the embed code inserted
html_file = create_html_file()

if tag_id in tag_id_list:
# Automatically open the generated HTML file in the web browser
    open_html_in_browser(html_file)
else:
    print("unrecognized RFID tag")

