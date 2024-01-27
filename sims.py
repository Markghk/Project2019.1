import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        pass


brands_of_car = {"BMW": {"fuel": 100, "strength": 100, "consumption": 12},
                 "Volvo": {"fuel": 80, "strength": 70, "consumption": 8},
                 "Ford": {"fuel": 70, "strength": 60, "consumption": 10},
                 "Ferrari": {"fuel": 60, "strength": 120, "consumption": 15}}
