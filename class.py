class personal:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print(self.name)
P1 = personal()
name = input("Please input your name:")
P1.set_name(name)
print("Your name is {}".format(P1.name))
print(P1.get_name())
P1.greet()
