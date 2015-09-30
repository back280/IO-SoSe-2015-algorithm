void setup() {
  int X = int (random (400, 700)); //generate random integer x-value between 400px and 700px
  int Y = int (random (400, 700));//generate random integer y-value between 400px and 700px
  size(X, Y); //creates a random background size within random X and Y
  int G = int(random(100, 200)); //defines an integer variable G with integer random values between 100 and 200
  background(G, G, G); // random greyish background color with the random value range between 100 and 200
  strokeWeight(1); //strock weight is 1 px
  stroke(255); //stroke color is white
  smooth(); // smoothes all schapes
}


void draw() { //defines the draw function
  int x = int (random (10, 500)); // creates X variable with random integer values between 10 and 500
  int y = int (random (10, 500)); // creates an Y variable with random integer values between 10 and 500
  int breite = int (random (5, 30)); // width defined as a integer random value between 5px and 30px
  ellipse(x, y, breite, breite); //defines a ellipese with random x, y and breite
  line(x, y, x+100, y+100); //this defines a line out of the circle center heading to the lower right 

  if (frameCount > 5) { //stops to loop after fifth frame
    noLoop();
  }

  saveFrame("line-######.png"); // Saves each frame as line-000001.png, line-000002.png, etc.
}
