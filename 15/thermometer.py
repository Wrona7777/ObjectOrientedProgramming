import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0.0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)

    def display(self):
        if self.is_on:
            message = f"Temperature: {self.temperature}C"
            if self.temperature >= 37.0:
                message += " (fever)"
            if self.temperature >= 41.0:
                message += " CRITICAL TEMPERATURE!!"
            print(message)