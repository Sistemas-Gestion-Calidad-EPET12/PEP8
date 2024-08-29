import random

def generate_random_numbers(count, min_value, max_value):
    """Genera una lista de números aleatorios dentro de un rango especificado.

    Args:
        count (int): Cantidad de números aleatorios a generar.
        min_value (int): Valor mínimo de los números aleatorios.
        max_value (int): Valor máximo de los números aleatorios.

    Returns:
        list: Una lista de números aleatorios generados.
    """
    numbers = []
    for _ in range(count):
        n = random.randint(min_value, max_value)
        numbers.append(n)
    return numbers


def bubble_sort(arr):
    """Ordena una lista en orden ascendente utilizando el algoritmo de ordenamiento por burbuja.

    Args:
        arr (list): Lista de números a ordenar.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def find_minimum(arr):
    """Encuentra el valor mínimo en una lista.

    Args:
        arr (list): Lista de números.

    Returns:
        int: El valor mínimo en la lista.
    """
    min_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
    return min_value


def find_maximum(arr):
    """Encuentra el valor máximo en una lista.

    Args:
        arr (list): Lista de números.

    Returns:
        int: El valor máximo en la lista.
    """
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value


def calculate_average(arr):
    """Calcula el promedio de los números en una lista.

    Args:
        arr (list): Lista de números.

    Returns:
        float: El promedio de los números en la lista.
    """
    total_sum = 0
    for i in arr:
        total_sum += i
    avg = total_sum / len(arr)
    return avg


def count_occurrences(arr, value):
    """Cuenta las ocurrencias de un valor específico en una lista.

    Args:
        arr (list): Lista de números.
        value (int): Valor a contar en la lista.

    Returns:
        int: El número de ocurrencias del valor en la lista.
    """
    count = 0
    for i in arr:
        if i == value:
            count += 1
    return count


def unique_values(arr):
    """Encuentra todos los valores únicos en una lista.

    Args:
        arr (list): Lista de números.

    Returns:
        list: Una lista de valores únicos.
    """
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique


def print_statistics(arr):
    """Imprime información estadística sobre una lista de números.

    Args:
        arr (list): Lista de números.
    """
    print("Estadísticas:")
    print("Mínimo:", find_minimum(arr))
    print("Máximo:", find_maximum(arr))
    print("Promedio:", calculate_average(arr))
    print("Ocurrencias del 5:", count_occurrences(arr, 5))
    print("Valores únicos:", unique_values(arr))


class NumberAnalyzer:
    """Analiza una lista de números y proporciona información estadística."""

    def __init__(self, numbers):
        """Inicializa el NumberAnalyzer con una lista de números.

        Args:
            numbers (list): Lista de números a analizar.
        """
        self.numbers = numbers
        self.sorted_numbers = []

    def analyze(self):
        """Analiza e imprime información estadística sobre los números."""
        print("Analizando números...")
        self.sorted_numbers = self.numbers.copy()
        bubble_sort(self.sorted_numbers)
        print_statistics(self.sorted_numbers)


def palindrome(word):
    """Verifica si una palabra es un palíndromo.

    Args:
        word (str): Palabra a verificar.

    Returns:
        bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    word = word.lower()
    return word == word[::-1]


def fibonacci(n):
    """Genera una secuencia de Fibonacci hasta n términos.

    Args:
        n (int): Número de términos en la secuencia de Fibonacci.

    Returns:
        list: La secuencia de Fibonacci.
    """
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
    """Calcula el factorial de un número.

    Args:
        n (int): El número para calcular su factorial.

    Returns:
        int: El factorial del número.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def find_primes(n):
    """Encuentra todos los números primos hasta un número dado.

    Args:
        n (int): El límite superior para encontrar números primos.

    Returns:
        list: Una lista de números primos hasta n.
    """
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
    """Imprime la secuencia de Fibonacci hasta n términos.

    Args:
        n (int): Número de términos en la secuencia de Fibonacci.
    """
    print("Secuencia de Fibonacci hasta", n, "términos:")
    print(fibonacci(n))


def print_prime_numbers(n):
    """Imprime todos los números primos hasta un número dado.

    Args:
        n (int): El límite superior para imprimir números primos.
    """
    print("Números primos hasta", n, ":")
    print(find_primes(n))


def main():
    """Función principal para ejecutar el programa."""
    numbers = generate_random_numbers(100, 1, 100)
    analyzer = NumberAnalyzer(numbers)
    analyzer.analyze()

    word = "racecar"
    if palindrome(word):
        print(word, "es un palíndromo")
    else:
        print(word, "no es un palíndromo")

    num = 10
    print_fibonacci_sequence(num)
    print_prime_numbers(50)
    print("Factorial de", num, ":", factorial(num))


if __name__ == "__main__":
    main()
