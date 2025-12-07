from tv import TV

def main():
    tv_set = TV()
    tv_set.turn_on()
    tv_set.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "HBO"])

    tv_set.show_status()
    
    tv_set.increase_volume()
    tv_set.increase_volume()
    tv_set.show_status()

    for i in range(10):
        tv_set.increase_volume()
    tv_set.show_status()

    tv_set.decrease_volume()
    tv_set.show_status()

    tv_set.set_channel(8)
    tv_set.show_status()
    
    tv_set.turn_off()

if __name__ == "__main__":
    main()