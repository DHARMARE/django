class Test:
    def __init__(self):
        print("initialising object")

    def __del__(self):
        print("dellocating the acquired memory")

t1 = Test()
del t1

print("next half of the code")