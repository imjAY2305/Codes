class Computer:
    def __init__(self,ram,cpu): #CONSTRUCTOR
        self.ram = ram
        self.cpu= cpu

    def config(self):
        print("MY PC",self.cpu,self.ram)

com1 = Computer(16,"3.2GHz") #Object Creation
com1.config()
print(com1.ram)