class Person:
    def __init__(self):
        pass

    def take_inputfromuser(self) -> object:
        self.name =input("enter your name:")
        self.age= int(input("enter your age:"))
        self.adress=input("enter your adress:")
    def display(self):
        print("Hello,I am",self.name,".I am",self.age,"years old. and live in",self.adress)

#p1=Person()
#p1.take_inputfromuser()
#p1.display()

for i  in range(1,3):
    i= Person()
    i.take_inputfromuser()
    i.display()


