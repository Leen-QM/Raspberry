import requests
import webbrowser
import os

# Your Sketchfab API key
api_key = "1a53843034804dfda647a3a20523b479"

# The model ID for the "Head from a Statue"
model_id = "9d3c60a68f014a4e9c44bb61f1e220d3"

def get_model_embed_code(model_id):
    # The API endpoint to get model details
    api_url = f"https://api.sketchfab.com/v3/models/{model_id}"

    # Set up the headers with your API key
    headers = {
        "Authorization": f"Token {api_key}"
    }

    # Make the GET request to the Sketchfab API
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Extract the viewer URL (this is the URL for embedding the model)
        viewer_url = data['viewerUrl']

        # Create the embed code using the viewer URL
        embed_code = f'<iframe width="100%" height="100%" src="{viewer_url}/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen></iframe>'
        
        return embed_code
    else:
        print("Error fetching model data")
        return None

def create_html_file(embed_code):
    # HTML template with the embed code inserted (full screen)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>3D Model Viewer</title>
        <style>
            body, html {{
                margin: 0;
                padding: 0;
                height: 100%;
                width: 100%;
                overflow: hidden;
            }}
            iframe {{
                width: 100%;
                height: 100%;
                border: none;
            }}
        </style>
    </head>
    <body>
        <!-- Embed the model here -->
        {embed_code}
    </body>
    </html>
    """

    # Write the content to an HTML file
    html_file = "model_viewer.html"
    with open(html_file, "w") as file:
        file.write(html_content)
        print(f"HTML file created successfully: {html_file}")

    return html_file

def open_html_in_browser(html_file):
    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{os.path.realpath(html_file)}")

# Get the embed code for the model
embed_code = get_model_embed_code(model_id)

if embed_code:
    # Create the HTML file with the embed code inserted
    html_file = create_html_file(embed_code)

    # Automatically open the generated HTML file in the web browser
    open_html_in_browser(html_file)
else:
    print("Failed to fetch embed code.")
