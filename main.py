from data import*
from tools import *


def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number


assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

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

def dec_math():
    init_base = init_target()[1]
    init_number = init_target()[0]
    if init_base == "bin":
        return bin_to_dec(init_number)
    elif init_base == "hex":
        return hex_to_dec(init_number)
    else:
        raise ValueError("Invalid base")



def bin_math():
    target_base = init_target()[2]
    init_base = init_target()[1]
    init_number = init_target()[0]
    if target_base == "bin" and init_base == "dec":
        return dec_to_bin(int(init_number, 2))
    elif target_base == "bin" and init_base == "hex" :
        return hex_to_bin(init_number)
    else:
        raise ValueError("Invalid base")


# target_number = \
#       bin_dec_hex__to__bin_dec_hex (init_number, \
#                                     init_base, \
#                                     target_base)




init_target ()



















