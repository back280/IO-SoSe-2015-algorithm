void setup() {
  size(600, 600); //define canavas size
  background(255, 255, 255); //define canavas background: white  
  noFill(); //no filling
  smooth();
  
}
void draw() { //define draw
  drawEllipse(); //start function drawEllipse() six times
  drawEllipse();
  drawEllipse();
  drawEllipse();
  drawEllipse();
  drawEllipse();
}
void drawEllipse() { //define the functon drawEllipse
  strokeWeight(1); //define stroke weight
  stroke(0, 0, 0);  //define stroke color: black
  int x = int (random (100, 500)); //generate random integer x-value between 100 and 500
  int y = int (random (100, 500)); //generate random integer y-value between 100 and 500
  int width = int (random (5, 30)); //generate random integer width between 5 and 30
  ellipse(x, y, width, width); //define ellipse based on the upper ramdom values x,y and width=height=circle 
  
  if (frameCount > 0) { //call draw fuction onlx one times
    noLoop();
  }
  // Saves each frame as line-000001.png, line-000002.png, etc.
  saveFrame("line-######.png"); //create image in png format

}
