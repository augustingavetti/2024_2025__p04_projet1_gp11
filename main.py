from data import*
from tools import *


def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number


assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

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
    init_base = ask_for_the_init_base ()
    for nb in init_base:
        if init_base == bin_valid_chars and init_number == bin_valid_chars:
            target_base
        elif init_base == dec_valid_chars and init_number == dec_valid_chars:
            target_base
        elif init_base == hex_valid_chars and init_number == hex_valid_chars:
            target_base
        else:
            print ("Entrée invalide! Entrez une nombre et une base valide s'il vous plait")
    target_base = ask_for_the_target_base ()
    
    
    if target_base == bin_valid_chars and target_base == dec_valid_chars and target_base ==  hex_valid_chars:
        hex_math
    elif target_base == bin_valid_chars and target_base ==  dec_valid_chars:
        dec_math
    else:
        bin_math

    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)




init_target ()
