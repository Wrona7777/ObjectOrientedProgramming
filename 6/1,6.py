class Phone:
    def __init__(self):
        self.is_on = False
        self.battery_level = 50
        self.volume = 5

    def turn_on(self):
        self.is_on = True

    def charge_battery(self, amount):
        self.battery_level += amount

    def set_volume(self, level):
        self.volume = level

smartphone = Phone()
smartphone.turn_on()
smartphone.charge_battery(20)
smartphone.set_volume(8)

print(f"Is ON: {smartphone.is_on}")
print(f"Battery: {smartphone.battery_level}")
print(f"Volume: {smartphone.volume}")