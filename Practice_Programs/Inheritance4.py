class Base:
    def fun(self):
        print("Inside Base Fun")

class Derived(Base):
   pass

dobj = Derived()

dobj.fun()
