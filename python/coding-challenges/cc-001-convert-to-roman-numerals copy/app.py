
def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman


is_invalid = False

while True:
    info = """
###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively : """

    alphanum = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()
    if not alphanum.isdecimal():
        if alphanum.lower() == 'exit':
            print('\nExiting the program... Good Bye')
            break
        else:
            is_invalid = True
            continue

    number = int(alphanum)
    if 0 < number < 4000:
        print(
            f'\nRoman numerals representation of decimal number "{alphanum}"" is equal to {convert(number)}')
        is_invalid = False
    else:
        is_invalid = True
