class Demo:
# Class Variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    #Instance Method
    def fun(self):
        print("Inside Instance Method Named As Fun...")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

    #Class Method
    @classmethod   
    def gun(cls):
        print("Inside Class Method Named As Gun...")
       #print(Demo.No1)
       #print(Demo.No2)
        print(cls.Value1)
        print(cls.Value2)

    #Static Method
    @staticmethod
    def sun():
        print("Inside Static Method Named As Sun...")
        print(Demo.Value1)
        print(Demo.Value2)

Demo.sun()
