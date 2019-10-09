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

r = Square(4)
print(s.area())		# returns 16

t = Square(5)
print(s.area())		# returns 25
