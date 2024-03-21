globalvalue = {"a":1}


def bad_function(x,b=globalvalue ):
  result=0
  b["a"]+=1
  for i in range(x):
    result += i
    
    return result

class BadClassName:
  def __init__(self,name ):
    self.name = name

  def get_name(self ):
    return self.name

  def set_name(self, new_name ):
    self.name = new_name

  
 