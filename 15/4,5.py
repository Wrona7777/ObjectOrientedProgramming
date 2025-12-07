from thermometer import Thermometer

def main():
    therm = Thermometer()
    therm.turn_on()
    therm.measure()
    therm.display()
    therm.turn_off()

if __name__ == "__main__":
    main()