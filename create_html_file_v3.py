def create_html_file():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>3D Model Viewer</title>
      <link rel="stylesheet" href="pagescroll_v2.css" />
      <script src="pagescroll_v2.js"></script> <!-- Link to the separate JS file -->

   </head>

<body>
<div class="scrollable">
  <div class="scroll left" onclick="left()"><</div>
  <div id="1" class="section part1">
        <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/war-mask-b91521402d6b48d7be9c4357be799699/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen onload="playAudio('audio1')"></iframe>
        <audio id="audio1" src="https://media.smartify.org/track_f9ghnUU47nuSwLlGdt0y/0H7W6OEz8sLj1LJca8Zb.mp3?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vbWVkaWEuc21hcnRpZnkub3JnL3RyYWNrX2Y5Z2huVVU0N251U3dMbEdkdDB5LzBIN1c2T0V6OHNMajFMSmNhOFpiLm1wMyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MTY1MTIwMH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQwMzU1MjAwfX19XX0_&Signature=kJuS4T6zhtQGEcQuBPHgvioLBgpDIRw1YvNWwjMKCxOIRyGfbVoOm-ARyqCyBhn8WZG~dWHekqP8TwdFrsM580Ydr-YHf8esaldXPJ1RASJRmzyj7ObxA1EFqOqqHLDeQ1XlTpOOgU~8xWRxZ3zRL2PVV7pgeF5593yxYIx2gzadcBBSl5~jXUOux3AYb3eIvpe~4L9ixBL0V7vJCCXjd-Z1bTBfV663-DEu0NclIMw0SUkSM9C0AupICpKx3mxxbV-Y1jxQpH3x26iXcp6qJ-wvAm5fScVHBG7x8f7A8v~bjL4u3AGILNrXsqOchBIetf3TMOoOhTQcyBTmVVWqHg__&Key-Pair-Id=K2TK72C9H46KK2"" preload="auto"></audio>
      </div>
  <div id="2" class="section part2">
        <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/head-from-a-statue-179efa76026045f096529d06c1c6fa98/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen onload="playAudio('audio2')"></iframe>
        <audio id="audio2" src="audio2.mp3" preload="auto"></audio>
      </div>
  <div id="3" class="section part3">
        <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/planispheric-astrolabe-e31eff18e6c74b2bb7be497f0ee04ecc/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen onload="playAudio('audio3')"></iframe>
        <audio id="audio3" src="audio3.mp3" preload="auto"></audio>
      </div>
 <div id="4" class="section part4">
        <iframe width="100%" height="100%" src="https://sketchfab.com/3d-models/fountainhead-94fa72eba5554df9919a7a27cee9b3b5/embed" frameborder="0" allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen onload="playAudio('audio4')"></iframe>
        <audio id="audio4" src="audio4.mp3" preload="auto"></audio>
      </div>  <div class="scroll right" onclick="right()">></div>
</div>
</body>

</html>
    """

      # Write the content to an HTML file
    html_file = "model_viewer.html"
    with open(html_file, "w") as file:
        file.write(html_content)
        print(f"HTML file created successfully: {html_file}")

    return html_file

