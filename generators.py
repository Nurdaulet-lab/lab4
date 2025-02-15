san=int(input())

class MyNumbers:
  def __iter__(self):
    self.a = 1
    self.b = 1
    return self

  def __next__(self):
    if self.a <= san*san:
      x = self.a
      self.b+=1
      self.a=self.b*self.b
      
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#2 esep
x=int(input())
class MyNumbers:
    def __iter__(self):
        self.a=1
        self.b=1
        return self
    
    def __next__(self):
        if self.a<=x:
            y=self.a
            self.a+=1
            return y
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)

for y in myiter:
    if y%2==0 and y!=x and y!=x-1:
        print(y,end=",")
    elif y%2==0:
        print(y)
#3 esep 
x=int(input())
class MyNumbers:
    def __iter__(self):
        self.a=1
        self.b=1
        return self
    
    def __next__(self):
        if self.a<=x:
            y=self.a
            self.a+=1
            return y
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)

for y in myiter:
    if y%3==0 and y%4==0 :
        print(y)
    
#4 esep
san1=int(input())
san2=int(input())
class MyNumbers:
  def __iter__(self):
    self.a = san1**2
    self.b = san1
    return self

  def __next__(self):
    if self.a <= san2*san2:
      x = self.a
      self.b+=1
      self.a=self.b*self.b
      
      return x
    else:
      raise StopIteration
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#esep 5
san=int(input())

class MyNumbers:
  def __iter__(self):
    self.a = san
    return self

  def __next__(self):
    if self.a >= 0:
      x = self.a
      self.a-=1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

