from os import system
def bitwise(oprator:str, number1:int, number2:int):
    print('\n||----------#*#----------||\n')
    print(f'| {str(number1).center(4)} in binery is: ', bin(number1))
    print(f'| {str(number2).center(4)} in binary is: ', bin(number2))
    print('|____________________________result')
    if oprator == '&':
        result = number1&number2
        return result
    elif oprator == '|':
        result = number1|number2
        return result
    elif oprator == '^':
        result = number1^number2
        return result
    elif oprator == '~':
        print(f'| {str(~number1).center(4)} in binary is:', bin(~number1))
        print(f'| {str(~number2).center(4)} in binary is:', bin(~number2))
        return None
    elif oprator == '>>':
        result = number1 >> number2
        return result
    elif oprator == '<<':
        result = number1 << number2
        return result

while True:
    number1 = int(input('enter first number  (type: int): '))
    number2 = int(input('enter second number (type: int): '))
    oprator = input('enter oprator type: [&, |, ^, ~, >>, <<]')

    result = bitwise(oprator, number1, number2)
    if type(result) == int:
        print(f'| {str(result).center(4)} in binary is: ', bin(result))
    input('(press enter)')
    system('clear')
    