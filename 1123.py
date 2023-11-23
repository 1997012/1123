class person:
    def __init__(self,n,g,a):
        self.name="Sam"
        self.gender="Male"
        self.age=22


    def talk(self):
        print("Hi I'm ",self.name)

    def vote(self):
        if self.age<18:
            print("I am not eligible to vote")
        else:
            print("I am eligible to vote")

obj1=person("Sam,Male",22)