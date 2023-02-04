class player:
  #hp=10;
  #atk=2;
  #bounc=10;
  def __init__(self, canv, x,y,color):
    self.x=x
    self.y=y
    self.color=color
    self.canv=canv
    self.hp=10
    self.atk=2
    self.bounc=100
    self.body=self.canv.create_oval(self.x-25,self.y-50,self.x+25,self.y,width=0,fill=self.color)
    
  def draw(self):
    self.body=self.canv.create_oval(self.x-25,self.y-50,self.x+25,self.y,width=0,fill=self.color)
  
  def jump(self):
    self.y+=self.bounc
    self.canv.move(self.body,0,self.bounc)
    