from data import*
from main import*
   
def dec_to_bin(init_number):
    n = init_number
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    result += "+1" if init_number % 2 == 1 else "+0"
    return result
            
       
def hex_to_bin(init_number):
    hex_to_binary= {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                } 
    result = ""
    for digit in init_number.upper():
        if digit in hex_to_binary:
            result += hex_to_binary[digit]
        else:
            raise ValueError(f"Invalid hexadecimal digit: {digit}")
        result = result.lstrip('0')
        if not result:
            return '0'
        last_digit = init_number[-1].upper()
        result += "+1" if int(hex_to_binary[last_digit], 2) % 2 == 1 else "+0"
        return result
    
def bin_to_dec(init_number):
    result = 0
    power = 0
    for digit in reversed(init_number):
        if digit == '1':
            result += 2 ** power
        power += 1
    return str(result)

def hex_to_dec(init_number):
    return str(int(init_number, 16))


def dec_to_hex(init_number):
    n = int(init_number)
    hex_digits = hex_valid_chars(n)
    result = ""
    while n > 0:
        result = hex_digits[n % 16] + result
        n = n // 16
    return result if result else "0"

def bin_to_hex(init_number):
    decimal = int(init_number, 2)
    return dec_to_hex(decimal)

