


class Random:
  def __init__( self, x, y ):
    self.x = x
    self.y = y
    print( x+y )
  
  def operation( self, z ):
    self.z = z 
    z = self.x + self.y + self.z
    print(z)
    
    
    
p = Random( 5, 6)
p.operation( 10 )
