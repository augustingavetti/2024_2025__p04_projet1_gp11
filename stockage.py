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

# def check_char_is_valid(char):
#     return char in base_valid_chars

# def is_a_valid_base(base):
#     i = 0
#     while is_valid_char:
#         is_valid_char = check_char_is_valid (base [i])
#         i = i + 1
#     return is_valid_char

# def ask_for_init_base():
#     init_base = input(ask_for_init_base_text)
#     while not (is_a_valid_base (init_base)):
#         init_base = input(ask_again_for_init_base_text)
#     return  init_base

# def ask_for_the_target_base():
#     init_target = input(ask_for_target_base_text)
#     while not (is_a_valid_base (init_target)):
#         init_target = input(ask_again_for_target_base_text)
#     return  init_target

# def verifier_entier_toutes_bases(nombre):
#     valide_base_2 = bin_valid_chars
#     valide_base_10 = dec_valid_chars
#     valide_base_16 = hex_valid_chars
    
#     bases_valides = []
#     if valide_base_2:
#         bases_valides.append(2)
#     if valide_base_10:
#         bases_valides.append(10)
#     if valide_base_16:
#         bases_valides.append(16)
    
#     if bases_valides:
#         if len(bases_valides) == 1:
#             bases_str = str(bases_valides[0])
#         elif len(bases_valides) == 2:
#             bases_str = f"{bases_valides[0]} ou {bases_valides[1]}"
#         else:
#             bases_str = f"{bases_valides[0]}, {bases_valides[1]} ou {bases_valides[2]}"




# def init_target ():
#     init_number = ask_for_init_number ()
#     init_base = ask_for_init_base ()
#     target_base = ask_for_the_target_base ()
#     return init_number, init_base, target_base