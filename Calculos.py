import random

def generate_random_numbers(count, min_value, max_value):
    """Generate a list of random numbers within a given range."""
    numbers = []
    for _ in range(count):
        n = random.randint(min_value, max_value)
        numbers.append(n)
    return numbers

def bubble_sort(arr):
    """Sort a list using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def find_minimum(arr):
    """Find and return the minimum value in a list."""
    min_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
    return min_value

def find_maximum(arr):
    """Find and return the maximum value in a list."""
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value

def calculate_average(arr):
    """Calculate and return the average of a list."""
    total_sum = 0
    for i in arr:
        total_sum += i
    avg = total_sum / len(arr)
    return avg

def count_occurrences(arr, value):
    """Count how many times a value appears in a list."""
    count = 0
    for i in arr:
        if i == value:
            count += 1
    return count

def unique_values(arr):
    """Return a list of unique values from the input list."""
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique

def print_statistics(arr):
    """Print statistics of a list, including min, max, average, and more."""
    print("Statistics:")
    print("Minimum:", find_minimum(arr))
    print("Maximum:", find_maximum(arr))
    print("Average:", calculate_average(arr))
    print("Occurrences of 5:", count_occurrences(arr, 5))
    print("Unique values:", unique_values(arr))

class NumberAnalyzer:
    """Analyze a list of numbers by sorting and printing statistics."""
    
    def __init__(self, numbers):
        """Initialize with a list of numbers."""
        self.numbers = numbers
        self.sorted_numbers = []
    
    def analyze(self):
        """Sort the numbers and print their statistics."""
        print("Analyzing numbers...")
        self.sorted_numbers = self.numbers.copy()
        bubble_sort(self.sorted_numbers)
        print_statistics(self.sorted_numbers)

def palindrome(word):
    """Check if a word is a palindrome."""
    word = word.lower()
    return word == word[::-1]

def fibonacci(n):
    """Generate a Fibonacci sequence of n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq

def factorial(n):
    """Calculate the factorial of a given number."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_primes(n):
    """Find and return a list of prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def print_fibonacci_sequence(n):
    """Print the Fibonacci sequence up to n terms."""
    print("Fibonacci sequence up to", n, "terms:")
    print(fibonacci(n))

def print_prime_numbers(n):
    """Print all prime numbers up to n."""
    print("Prime numbers up to", n, ":")
    print(find_primes(n))

def main():
    """Main function to run the number analysis and other tests."""
    numbers = generate_random_numbers(100, 1, 100)
    analyzer = NumberAnalyzer(numbers)
    analyzer.analyze()

    word = "racecar"
    if palindrome(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

    num = 10
    print_fibonacci_sequence(num)
    print_prime_numbers(50)
    print("Factorial of", num, ":", factorial(num))

if __name__ == "__main__":
    main()
