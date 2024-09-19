import random

def generate_random_numbers(count, minvalue, maxValue):    
    numbers = []
    for i in range(count):
        number = random.randint(minvalue, maxValue)
        numbers.append(number)
    
    return numbers

def bubble_sort(arr):
    
    array = len(arr)
    
    for i in range(array - 1):
        for j in range(0, array - i - 1):
            if arr[j] > arr[ j + 1 ]:
                arr[j], arr[ j + 1 ] = arr[ j + 1], arr[j]

def find_minimum(arr):
    min_value = arr[0]
    
    for i in arr:
        if i < min_value:
            min_value = i
    
    return min_value

def find_maximum(arr):
    
    maxvalue = arr[ 0 ]
    for numero in arr:
        if numero > maxvalue:
            maxvalue = numero
    return maxvalue

def calculate_average(arr):
    s = 0
    for i in arr:
        s += i
        avg = s / len(arr)
    return avg

def count_occurrences(arr, value):
    count = 0
    for i in arr:
        if i == value:
            count += 1
    return count

def unique_values(arr):
    
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique

def print_statistics(arr):
    print("Statistics:")
    print("Minimum:", find_minimum(arr))
    print("Maximum:", find_maximum(arr))
    print("Average:", calculate_average(arr))
    print("Occurrences of 5 numbers :", count_occurrences(arr, 5))
    print("Unique values:", unique_values(arr))

class NumberAnalyzer: 
    def __init__(self, numbers):
        self.numbers = numbers
        self.sorted_numbers = []
    
    def analyze(self):
        print("Analyzing numbers...")
        self.sorted_numbers = self.numbers.copy()
        bubble_sort(self.sorted_numbers)
        print_statistics(self.sorted_numbers)

def palindrome(word):
    word = word.lower()
    return word == word[::-1]

def fibonacci(n):
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

def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def find_primes(number):
    primes = []
    for num in range(2 , number + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def print_fibonacci_sequence(number):
    print("Fibonacci the result is the sequence up to: ", number, " terms:")
    print(fibonacci(number))

def print_prime_numbers(number):
    print("Prime numbers up to", number, ":")
    print(find_primes(number))

def main():
    numbers = generate_random_numbers(100, 1, 100)
    analyzer = NumberAnalyzer(numbers)
    analyzer.analyze()

    word = "racecar"
    if palindrome(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

    number = 10
    print_fibonacci_sequence(number)
    print_prime_numbers(50)
    print("Factorial of ", number, ": ", factorial(number))

if __name__ == "__main__":
    main()