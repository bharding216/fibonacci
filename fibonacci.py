def fibonacci(x, n):
    fib_list = [0, 1]

    while True:
        next_value = fib_list[-1] + fib_list[-2]
        if next_value <= x:
            fib_list.append(next_value)
        else:
            break

    first_fib_number = fib_list[-1] + fib_list[-2]
    second_fib_number = first_fib_number + fib_list[-1]

    if n == 0:
        return 'Please select a value of "n" greater than zero.'

    if n == 1:
        return [first_fib_number]

    result = [first_fib_number, second_fib_number]
    
    while n > len(result):
        next_value = result[-1] + result[-2]
        result.append(next_value)

    return result

x = int(input('Enter value for x: '))
n = int(input('Enter value for n: '))

output = fibonacci(x, n)
print(output)
