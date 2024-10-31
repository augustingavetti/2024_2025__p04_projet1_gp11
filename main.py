from data import*
from tools import*

def check_char_is_valid(char):
    return char in base_valid_chars

def is_a_valid_base(base):
    i = 0
    while is_valid_char:
        is_valid_char = check_char_is_valid (base [i])
        i = i + 1
    return is_valid_char

def ask_for_init_base():
    init_base = input(ask_for_init_base_text)
    while not (is_a_valid_base (init_base)):
        init_base = input(ask_again_for_init_base_text)
    return  init_base

def ask_for_the_target_base():
    init_target = input(ask_for_target_base_text)
    while not (is_a_valid_base (init_target)):
        init_target = input(ask_again_for_target_base_text)
    return  init_target

def check_char_is_valid(char):
    return char in hex_valid_chars

def is_a_valid_number(number):
    i = 0
    while is_valid_char:
        is_valid_char = check_char_is_valid (number [i])
        i = i + 1
    return is_valid_char

def ask_for_init_number():
    init_number = input(ask_for_init_number_text)
    while not (is_a_valid_number (init_number)):
        init_number = input(ask_again_for_init_number_text)
    return  init_number


def init_target ():
    init_number = ask_for_init_number ()
    init_base = ask_for_init_base ()
    target_base = ask_for_the_target_base ()
    return init_number, init_base, target_base


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

def bin_dec_hex_to_bin_dec_hex():
    result = dec_to_hex(result) or bin_to_dec(result) or hex_to_dec(result) or hex_to_bin(result)
    return result

def end():
    init_number, init_base, target_base = init_target()
    init_base = int(init_base)
    target_base = int(target_base)
    result = convert_base(init_number, init_base, target_base)
    print(f"{init_number} in base {init_base} is equal to {result} in base {target_base}")
