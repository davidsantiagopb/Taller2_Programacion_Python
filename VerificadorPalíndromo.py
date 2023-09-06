def is_palindrome(num):
    original_num = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original_num == reverse

num = int(input("Ingrese un número: "))

if is_palindrome(num):
    print(f"{num} es un palíndromo.")
else:
    print(f"{num} no es un palíndromo.")