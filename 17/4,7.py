from statistics import Statistics

def main():
    stats = Statistics()
    
    data = [12, 37, 6, 9, 17]
    
    for number in data:
        stats.add_number(number)
        
    stats.display_numbers()
    stats.print_statistics()

if __name__ == "__main__":
    main()