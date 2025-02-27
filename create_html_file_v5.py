def create_html_file(language):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>3D Model Viewer</title>
      <link rel="stylesheet" href="pagescroll_v3.css" />
      <script src="pagescroll_v3.js" defer></script> <!-- Link to the separate JS file -->
    </head>

    <body>
    <div class="scrollable">
      <div class="scroll left" onclick="left()"><</div>
      <div id="1" class="section part1">
            <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/war-mask-b91521402d6b48d7be9c4357be799699/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen></iframe>
            <audio id="audio1" src="Object 1 {language}.mp3" preload="auto"></audio>
            <div class="audio-icon" onclick="toggleAudio('audio1', this)"></div>
          </div>
      <div id="2" class="section part2">
            <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/head-from-a-statue-179efa76026045f096529d06c1c6fa98/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen></iframe>
            <audio id="audio2" src="Object 2 {language}.mp3" preload="auto"></audio>
            <div class="audio-icon" onclick="toggleAudio('audio2', this)"></div>
          </div>
      <div id="3" class="section part3">
            <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/planispheric-astrolabe-e31eff18e6c74b2bb7be497f0ee04ecc/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen></iframe>
            <audio id="audio3" src="Object 3 {language}.mp3" preload="auto"></audio>
            <div class="audio-icon" onclick="toggleAudio('audio3', this)"></div>
          </div>
      <div id="4" class="section part4">
            <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/fountainhead-94fa72eba5554df9919a7a27cee9b3b5/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen></iframe>
            <audio id="audio4" src="Object 4 {language}.mp3" preload="auto"></audio>
            <div class="audio-icon" onclick="toggleAudio('audio4', this)"></div>
          </div>
      <div class="scroll right" onclick="right()">></div>
    </div>
    </body>

    </html>
    """
    html_file = "model_viewer.html"
    with open(html_file, "w") as file:
        file.write(html_content)
        print(f"HTML file created successfully: {html_file}")

    return html_file
