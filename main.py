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
    for elmt in init_base:
        if init_base == [0, 1] and init_number == [0, 1]:
            target_base
        elif init_base == decimal and init_number == decimal:
            target_base
        elif init_base == binary and init_number == binary:
            target_base
        else:
            print ("Invalid input! Please enter a valid number and base.")
    target_base = ask_for_the_target_base ()
    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)

init_target ()
