from data import *
from tools import *

def check_base(base):
    if base in ["2", "10", "16"]:
        return int(base)
    else:
        print(ask_again_for_init_base_text)
        return None

def is_valid_number(nombre, base):
    if base == 2:
        valid_chars = '01'
    elif base == 10:
        valid_chars = '0123456789'
    elif base == 16:
        valid_chars = '0123456789ABCDEFabcdef'
    else:
        return False
    return all(char in valid_chars for char in nombre)

def check_target(target):
    if target in ["2", "10", "16"]:
        return int(target)
    else:
        print(ask_again_for_target_base_text)
        return None

def convert_base(init_number, init_base, target_base):
    if init_base == 2:
        if target_base == 10:
            return bin_to_dec(init_number)
        elif target_base == 16:
            return bin_to_hex(init_number)
    elif init_base == 10:
        if target_base == 2:
            return dec_to_bin(int(init_number))
        elif target_base == 16:
            return dec_to_hex(int(init_number))
    elif init_base == 16:
        if target_base == 2:
            return hex_to_bin(init_number)
        elif target_base == 10:
            return hex_to_dec(init_number)
    raise ValueError(f"Conversion from base {init_base} to base {target_base} is not supported")

def main():
    nombre = input(ask_for_init_number_text)
    base = input(ask_for_init_base_text)
    target = input(ask_for_target_base_text)

    init_base = check_base(base)
    target_base = check_target(target)
    
    if init_base is None or target_base is None:
        return
    
    if not is_valid_number(nombre, init_base):
        print(ask_again_for_init_number_text)
        return
    
    result = convert_base(nombre, init_base, target_base)
    print(f"{nombre} in base {init_base} is equal to {result} in base {target_base}")

if __name__ == "__main__":
    main()