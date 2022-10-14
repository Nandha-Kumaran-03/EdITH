var yoff = 0.0;
var rX=15;
var rY=60;
function setup() {
  createCanvas(800, 600,WEBGL);
  background(0);
}

function draw() {
  
  rotateX(radians(rX));
  rotateY(radians(rY));
  //translate(width / 2, height / 2);
  if (rX<=360) {
    rX+=.1;
  }
  else {
    rX=0;
  }
  if (rY<=360) {
    rY+=.1;
  }
  else {
    rY=0;
  }
  var radius = 150;

  beginShape();
  var xoff = 0;
  for (var a = 0; a < TWO_PI; a += 0.1) {
    var offset = map(noise(xoff, yoff), 0, 1, -25, 25);
    var r = radius + offset;
    var x = r * cos(a);
    var y = r * sin(a);
    vertex(x, y);
    xoff += 0.1;
    //ellipse(x, y, 4, 4);
  }
  endShape();

  yoff += 0.01;
}