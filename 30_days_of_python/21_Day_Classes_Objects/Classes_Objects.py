class Robot: 
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

#r1 = Robot()
#r1.name = "Zonique"
#r1.color = "silver"
#r1.weight = 40

#r2 = Robot()
#r2.name = "C-3PO"
#r2.color = "gold"
#r2.weight = 75


r1=Robot("Zonique", "silver", 40)
r2=Robot("C-3PO", "gold", 75)

r1.introduce_self()
r2.introduce_self() 


#output: My name is Zonique
#output: My name is C-3PO