from tri import Tri                                             #import external data 
def setup():                                                    #define the setup
    #noFill()                                                   ##nofilling
    size(600, 600)                                              #canvas size 600px by 600px 
 
    tri1 = Tri(PVector(50,50),PVector(180,180),PVector(60,300)) #defines triangle one with three different PVector
    tri2 = Tri(tri1.p3,tri1.p2,PVector(350,350))                #defines triangle two 
    tri3 = Tri(tri2.p3,tri2.p2,PVector(180,30))                 #defines triangle three
    tri4 = Tri(tri3.p3,PVector(400,100),tri3.p1)                #defines triangle four 
    tri5 = Tri(tri3.p3,tri1.p1,tri1.p2)                         #defines triangle five
    
    tri6_inner = Tri(tri4.p2,tri4.calc_mid3(),tri3.p1)          #defines the inner triangle of triangle 4 through: point 2, the mid between point 1 and point 3 and the final point 1
    tri7_inner = Tri(tri1.p1,tri1.calc_mid2(),tri1.calc_mid1()) #defines the inner triangle of triangle 1 through: point 2, the mid between point 3 and point 3 the mid between point 2 and point 2
    tri8_inner = Tri(tri1.p1,tri1.calc_mid3(),tri1.calc_mid2()) #efines the inner triangle of triangle 1 through: point 2, the mid between point 3 and point 3 the mid between point 2 and point 2
    
    tri1.draw_triangle(250,0,0)                                 #draws triangle one: calls draw_triangle function with R,G,B filling and coordinate of tri1 (triangle one) 
    tri2.draw_triangle(255,234,0)                               #draws triangle two: calls draw_triangle function with R,G,B filling and coordinate of tri2 (triangle two)
    tri3.draw_triangle(86,236,164)                              #draws triangle three: calls draw_triangle function with R,G,B filling and coordinate of tri3 (triangle three)
    tri4.draw_triangle(250,250,250)                             #draws triangle four: calls draw_triangle function with R,G,B filling and coordinate of tri4 (triangle four)
    tri5.draw_triangle(141,130,248)                             #draws triangle five: calls draw_triangle function with R,G,B filling and coordinate of tri5 (triangle five)
    
    tri6_inner.draw_triangle(123,44,45)                         #draws inner triangle one through draw_triangle function with R,G,B filling
    tri7_inner.draw_triangle(13,55,110)                         #draws inner triangle two through draw_triangle function with R,G,B filling
    tri8_inner.draw_triangle(186,19,123)                        #draws inner triangle three through draw_triangle function with R,G,B filling
    
    
    tri1.display_ellipse()                                      #draws ellipses of triangle one through dsiplay ellipse function
    #tri2.display_ellipse(255)
    #tri3.display_ellipse(255)
    tri4.display_ellipse()                                      #draws ellipses of triangle four through dsiplay ellipse function 
    #tri5.display_ellipse(255)
    
    saveFrame()                                                 #Save Frame function as tiff

    # executed once
#def draw():
    # executed all the time
    
#circle packing processing
#parralel lines
