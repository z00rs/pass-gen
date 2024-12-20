import random

# Функция для генерации случайных паролей
def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choices(characters, k=length))
    return password

# Функция для проверки, является ли число простым
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Функция для вывода всех простых чисел в заданном диапазоне
def list_primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

# Пример использования
if __name__ == "__main__":
    # Генерация случайного пароля
    print("Generated password:", generate_password())

    # Поиск простых чисел в диапазоне от 10 до 50
    primes = list_primes_in_range(10, 50)
    print("Prime numbers between 10 and 50:", primes)
