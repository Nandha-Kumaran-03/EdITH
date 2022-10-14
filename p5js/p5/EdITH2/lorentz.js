var x=0.01;
var y=0;
var z=0;

var p=10;
var q=28;
var r=8.0/3.0;


function setup() {
 
  createCanvas(windowWidth, windowHeight,WEBGL);
  background("#000000");
}
 
function draw() {
  
  var dt=0.01;

  var dx=(p*(y-x))*dt;
  x=x+dx;

  var dy=(x*(q-z)-y)*dt;
  y=y+dy;

  var dz=(x*y-r*z)*dt;
  z=z+dz;

  
  scale(4);
  stroke(255);
  
  rotateX(radians(60));
  rotateY(radians(15));

  var a = point(x,y,z);
  

  
}