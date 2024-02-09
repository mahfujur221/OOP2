numbers = [1, 3, 9, 2, 7, 11, 17, 21]

index = 0

while index < len(numbers):

    current_number = numbers[index]

    if current_number % 2 == 0:

        print('An even number', current_number, 'is found at index', index)
        break

    index += 1
else:
    print('No even number is found in the list. All numbers are odd.')

