class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_recipents(self):
        print(f"Distance: {self.distance}, Rate: {self.rate_per_km}, fare: {self.fare}")


def main():
    taxi1 = TaxiRide(10)
    taxi1.calculate_fare(300)
    taxi1.print_recipents()

    taxi2 = TaxiRide(40)
    taxi2.calculate_fare(50)
    taxi2.print_recipents()

if __name__ == "__main__":
    main()
