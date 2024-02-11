class Razer:
    def __init__(self):
        super().__init__()
        self.buttons = 6
        self.logotype = "Razer 3 snakes"
        self.company = "Razer"
class Wired:
    def __init__(self):
        super().__init__()
        self.wired = "Wired mouse"
        self.rgb = "Have rgb"
class Mouse(Razer, Wired):
    def printer(self):
        print(self.buttons)
        print(self.logotype)
        print(self.rgb)
        print(self.wired)
        print(self.company)

razer = Mouse()
razer.printer()