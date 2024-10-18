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
    