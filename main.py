from data import*
from tools import *


def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number


assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

def init_target ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    for nb in init_base:
        if init_base == bin_valid and init_number == bin_valid:
            target_base
        elif init_base == dec_valid and init_number == dec_valid:
            target_base
        elif init_base == hex_valid and init_number == hex_valid:
            target_base
        else:
            print ("Invalid input! Please enter a valid number and base.")
    target_base = ask_for_the_target_base ()
    if target_base == bin_valid and target_base == dec_valid and target_base ==  hex_valid:
        hex_math
    elif target_base == bin_valid and target_base ==  dec_valid:
        dec_math
    else:
        bin_math

    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)

init_target ()
