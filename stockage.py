# def dec_math():
#     init_base = init_target()[1]
#     init_number = init_target()[0]
#     if init_base == 2:
#         return bin_to_dec(init_number)
#     elif init_base == 16:
#         return hex_to_dec(init_number)
#     else:
#         raise ValueError("Invalid base")



# def bin_math():
#     target_base = init_target()[2]
#     init_base = init_target()[1]
#     init_number = init_target()[0]
#     if target_base == 2 and init_base == 10:
#         return dec_to_bin(int(init_number, 2))
#     elif target_base == 2 and init_base == 16 :
#         return hex_to_bin(init_number)
#     else:
#         raise ValueError("Invalid base")
    

# def hex_math():
#     target_base = init_target()[2]
#     init_base = init_target()[1]
#     init_number = init_target()[0]
#     if target_base == 16 and init_base == 10:
#         return dec_to_hex(int(init_number, 10))
#     elif target_base == 16 and init_base == 2:
#         return bin_to_hex(init_number)
#     else:
#         raise ValueError("Invalid base")
    

# def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
#     target_number = None
#     return target_number

# target_number = \
#     bin_dec_hex_to_bin_dec_hex (init_number, \
#                                 init_base, \
#                                 target_base,\
#                                 target_number)


# def is_a_valid_base(base):
#     for char in base:
#         if not check_char_is_valid(char):
#             return False
#     return True

# def is_a_valid_number(number):
#     for char in number:
#         if not check_char_is_valid(char):
#             return False
#     return True