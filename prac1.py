class Shape(object):
   def __init__(self):
       pass
 
   def area(self):
       return 0
 
class Square(Shape):
   def __init__(self,length):
       self.length = length
       Shape.__init__(self)
 
   def area(self):
       return self.length * self.length
 
s = Square(2)
print(s.area())		# returns 4
