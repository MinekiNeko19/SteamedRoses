class player:
  #hp=10;
  #atk=2;
  #bounc=10;
      
  hp=10
  atk=2
  def __init__(self, canv, x,y,color):
    self.x=x
    self.y=y
    self.color=color
    self.canv=canv
    self.dy=15
    self.dx=10
    self.body=self.canv.create_oval(self.x-10,self.y-20,self.x+10,self.y,width=0,fill=self.color)
    
  def draw(self):
    self.body=self.canv.create_oval(self.x-25,self.y-50,self.x+25,self.y,width=0,fill=self.color)
  
  def jump(self):
    
    self.canv.move(self.body,0,self.dy)
    self.y-=self.dy 
    self.dy-=5 
    
    
    