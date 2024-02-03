import random


class Pets:
    def __init__(self, name):
        self.name = name
        self.thirst = 0
        self.hungry = 0
        self.gladness = 50
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.hungry -= 35
        self.gladness += 15

    def to_drink(self):
        print("Time to drink")
        self.thirst -= 35
        self.gladness += 15

    def to_chill(self):
        print("Time to chill")
        self.gladness += 5
        self.hungry += 20
        self.thirst += 10

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 15

    def is_alive(self):
        if self.hungry > 90:
            print("Very hungry...Die...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.gladness > 80:
            print("I love you my owner")
            self.alive = True
        elif self.thirst > 75:
            print("Very thirst..Die...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Thirst = {self.thirst}")
        print(f"Hungry = {self.hungry}")

    def live(self, day):
        d = f"Day {day} of {self.name} life"
        print(f"{d:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_drink()
        self.end_of_day()
        self.is_alive()


cat = Pets("Пушок")
for day in range(1, 366):
    if cat.alive == False:
        break
    cat.live(day)
