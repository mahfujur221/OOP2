def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


while True:
    try:
        num = int(input("Enter a number (enter 0 to exit): "))

        if num == 0:
            print("Exiting the program.")
            break

        if is_prime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
