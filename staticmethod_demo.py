class StaticMethodDemo:
    @staticmethod #denotes the underlying method as of static type
    def add(x,y):
        print("Addition: ",(x+y))

StaticMethodDemo.add(15,5)