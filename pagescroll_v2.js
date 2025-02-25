var selected = 1;

function playAudio(id) {
  var audio = document.getElementById(id);
  audio.load();
  audio.play();
}

window.onkeyup = function(e) {
  if (e.key == 'ArrowRight') {
    right();
  } else if (e.key == 'ArrowLeft') {
    left();
  }
}

function left() {
  var section1 = document.getElementById('1');
  var section2 = document.getElementById('2');
  var section3 = document.getElementById('3');
  var section4 = document.getElementById('4');

  if (selected == 2) {
    section1.style.left = '0vw';
    section2.style.left = '100vw';
    section3.style.left = '200vw';
    section4.style.left = '300vw';
    
    selected = 1;
  } else if (selected == 3) {
    section1.style.left = '-100vw';
    section2.style.left = '0vw';
    section3.style.left = '100vw';
    section4.style.left = '200vw';
    
    selected = 2;
  } else if (selected == 4) {
    section1.style.left = '-200vw';
    section2.style.left = '-100vw';
    section3.style.left = '0vw';
    section4.style.left = '100vw';
    
    selected = 3;
  }
}

function right() {
  var section1 = document.getElementById('1');
  var section2 = document.getElementById('2');
  var section3 = document.getElementById('3');
  var section4 = document.getElementById('4');

  if (selected == 1) {
    section1.style.left = '-100vw';
    section2.style.left = '0vw';
    section3.style.left = '100vw';
    section4.style.left = '200vw';
    
    selected = 2;
  } else if (selected == 2) {
    section1.style.left = '-200vw';
    section2.style.left = '-100vw';
    section3.style.left = '0vw';
    section4.style.left = '100vw';
    
    selected = 3;
  } else if (selected == 3) {
    section1.style.left = '-300vw';
    section2.style.left = '-200vw';
    section3.style.left = '-100vw';
    section4.style.left = '0vw';
    
    selected = 4;
  }
}
