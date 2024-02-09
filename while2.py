total_sum = 0
count = 0

while True:
    user_input = input('Enter a number: ')

    if user_input.lower() == 'exit':
        break

    number = float(user_input)

    total_sum += number

    count += 1

average = total_sum / count if count > 0 else 0

print('Average:', average)
