let detailX;
let detailY;
// slide to see how detailX works
function setup() {
  createCanvas(windowWidth,800, WEBGL);
  detailX = createSlider(10, 30, 10);
  detailY = createSlider(10,30,10);
  detailX.position(10, height + 5);
  detailY.position(10, height+25);
  detailX.style('width', '80px');
  detailY.style('width', '80px');
  
  describe(
    'a white sphere with low detail on the x-axis, including a slider to adjust detailX'
  );
}

function draw() {
  background(0,0,0);
  rotateY(millis() / 1000);
  sphere(100, detailX.value(), detailY.value());
}