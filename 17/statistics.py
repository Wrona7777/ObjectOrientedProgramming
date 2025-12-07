class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print(" ".join(map(str, self.numbers)))

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)

    def calculate_mean(self):
        return sum(self.numbers) / len(self.numbers)

    def calculate_median(self):
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

    def print_statistics(self):
        print(f"Min: {self.get_min()}")
        print(f"Max: {self.get_max()}")
        print(f"Mean: {self.calculate_mean()}")
        print(f"Median: {self.calculate_median()}")