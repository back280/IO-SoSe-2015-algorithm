class Tri(object):                #declerates the class named Tri     
    p1 = PVector(0,0)             #defining seven Pvector with coordinates (0/0)
    p2 = PVector(0,0)
    p3 = PVector(0,0)
    p4 = PVector(0,0)
    p5 = PVector(0,0)
    p6 = PVector(0,0)
    p7 = PVector(0,0)
    
    w_p1 = int(random(10,50))          #defines randomized width for ellipse on point 1 between 10 and 50
    h_p1 = w_p1                        #defines height equals width for ellipse on point 1
    
    w_p2 = int(random(10,50))          #defines randomized width for ellipse on point 1 between 10 and 50
    h_p2 = w_p2                        #defines height equals width for ellipse on point 1
    
    w_p3 = int(random(10,50))          #defines randomized width for ellipse on point 1 between 10 and 50
    h_p3 = w_p3                        #defines height equals width for ellipse on point 1
    
    def __init__(self, point1, point2, point3): #Dont get what this is doing
        self.p1 = point1                  #constructor
        self.p2 = point2
        self.p3 = point3                               
        


    def draw_triangle(self, R,G,B):     #method of class display, defines the draw triangle function
        fill(R,G,B)                     #filling values with handover R,G,B 
        beginShape()                    #intilialises the shape
        vertex(self.p1.x,self.p1.y)     #creates a vertex with point one x values and point one y values
        vertex(self.p2.x,self.p2.y)     #creates a vertex with point two x values and point two y values
        vertex(self.p3.x,self.p3.y)     #creates a vertex with point three x values and point three y values
        endShape(CLOSE)                 #closes shape 
        
    def display_ellipse(self):                                    #method of class display. defines the ellipse function to draw ellipse. Handover R,G,B values deactivaded (self, R,G,B)
        noFill()                                                  #plain circles no filling only stroke line
        #fill(R,G,B)                                              #fill(R,G,B)
        ellipse(self.p1.x, self.p1.y, self.w_p1, self.h_p1)       #creates the ellipse with center point one x and y values and random height and width see beginning
        ellipse(self.p2.x, self.p2.y, self.w_p2, self.h_p2)       #creates the ellipse with center point two x and y values and random height and width see beginning
        ellipse(self.p3.x, self.p3.y, self.w_p3, self.h_p3)       #creates the ellipse with center point three x and y values and random height and width see beginning
        
    
    def calc_mid1(self):                                          #defines the function to calculate the mid between two vectors in an triangle. Here the center between point one and two
        xmid = (self.p1.x + self.p2.x) / 2
        ymid = (self.p1.y + self.p2.y) / 2        
        return PVector(xmid, ymid)                                #so we have a new point             
    
    def calc_mid2(self):                                          #defines the function to calculate the mid between two vectors in an triangle. Here the center between point two and three
        xmid = (self.p2.x + self.p3.x) / 2
        ymid = (self.p2.y + self.p3.y) / 2        
        return PVector(xmid, ymid)                                #so we have a new point
    
    def calc_mid3(self):                                          #defines the function to calculate the mid between two vectors in an triangle. Here the center between point three and one
        xmid = (self.p3.x + self.p1.x) / 2
        ymid = (self.p3.y + self.p1.y) / 2        
        return PVector(xmid, ymid)                                #so we have a new point
    

    
   
       
        
            
