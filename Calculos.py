import random

def generate_random_numbers(count, minvalue, maxValue):
    numbers = []
    for i in range(count):
        number = random.randint(minvalue, maxValue)
        numbers.append(number)
    return numbers

def bubbleSort(array):
    lista = len(array)
    for num in range(lista-1):
        for valor in range(0, num-lista-1):
            if array [valor] > array [valor+1]:
                array [valor], array [valor+1] = array [valor+1], array [valor]

def find_minimum(array):
    min_value = array[0]
    for numero in array:
        if numero < min_value:
            min_value = numero
    return min_value

def find_maximum(array):
    maxValue = array[0]
    for numero in array:
        if numero > maxValue:
            maxValue = numero
    return maxValue

def calculate_average(array):
    valor = 0
    for numero in array:
        valor += numero
    avg = valor / len(array)
    return avg

def count_occurrences(array, value):
    count = 0
    for numero in array:
        if numero == value:
            count += 1
    return count

def unique_values(array):
    unique = []
    for numero in array:
        if numero not in unique:
            unique.append(numero)
    return unique
######################################################################################################################################################
def print_statistics(array):
    print("Statistics:")
    print("Minimum:", find_minimum(array))
    print("Maximum:", find_maximum(array))
    print("Average:", calculate_average(array))
    print("Occurrences of 5 numbers :", count_occurrences(array, 5))
    print("Unique values:", unique_values(array))


class number_analyzer: 
    def __init__(self, numbers):
        self.numbers = numbers
        self.sorted_numbers = []
    
    def analyze(self):
        print("Analyzing numbers...")
        self.sorted_numbers = self.numbers.copy()
        bubbleSort(self.sorted_numbers)
        print_statistics(self.sorted_numbers)


def palindrome(word):
    word = word.lower()
    return word== word[:: -1]

def fibonacci(number):
    if number <= 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < number:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence
########################################################################################################
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num **0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def print_fibonacci_sequence(n):
    print("Fibonacci the result is the sequence up to", n, "terms:")
    print(fibonacci(n))

def print_prime_numbers(n):
    print("Prime numbers up to", n, ":")
    print(find_primes(n))

def main():
    numbers = generate_random_numbers(100, 1, 100)
    analyzer = number_analyzer(numbers)
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