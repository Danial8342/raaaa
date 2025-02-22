def stop_after_zero():
    sum_number = 0
    while True:
        number = int(input('enter your number'))
        if number == 0:
            print(f'sum numbers = {sum_number}')
            break
        else:
            sum_number =  sum_number + number

stop_after_zero()



def multiply_all(*args):
    multiply_all_numbers = 1
    for element in args:
        multiply_all_numbers = multiply_all_numbers * element
    return multiply_all_numbers

print(multiply_all(2, 3, 3))
