class Bird:
    def __init__ (self):
        print("Bird is Ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready")
    def whoisThis(self):
        print("Penguin")
    def run (self):
        print("Run Faster!")
peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()