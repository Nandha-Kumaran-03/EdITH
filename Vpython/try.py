from vpython import *

b = box(color=vector(100,100,100),pos=vector(0,10,10),size=vector(1,1,1))
a = arrow(pos=vector(0,0,0),up=b.pos,color=vector(255,255,255),len=5)