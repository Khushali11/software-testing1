class Car:
    def __init__(self, name: object, car_name: object) -> object:
        self.name = name
        self.car_name = car_name

    # method
    def mycar(self) -> object:
        print("hello,My name is ", self.name, "and i have a car name", self.car_name)

    def mycar_cost(self, amount: object) -> object:
        print("its cost is", amount)

    def mycar_costwithgst(self, amount=0) -> object:
        sum = amount + 2400000
        print(self.name, "car cost with gst:", sum)

    def mycar_size(self):
        size = 'small'
        print(self.name, "have a", size, "car")

    def mycar_color(self, color):
        print(self.name, " car color is ", color)


# creating object and invoking the constructor
p1 = Car("john", "suzuki")
p2 = Car("suzen", "creta")
p3 = Car("jorden", "TaTa nano")
p4 = Car("isha", "Tesla")
p5 = Car("mayank", "inova")
# accessing the object attributes
print(p1.name)
print(p2.name)

# invoking the object method
p1.mycar()
p1.mycar_cost(120000)
p2.mycar()
p2.mycar_color('red')
p3.mycar()
p3.mycar_size()  # no attribute, so every time small
p4.mycar()
p4.mycar_costwithgst(10000)
p4.mycar_costwithgst()
p5.mycar()
