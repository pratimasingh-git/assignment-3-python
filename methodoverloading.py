class Demo:
    def add(self, a=0, b=0):
        return a + b

d = Demo()
print(d.add(5))      # one argument
print(d.add(5, 10))  # two arguments
