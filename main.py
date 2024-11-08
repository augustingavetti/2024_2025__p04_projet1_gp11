from data import *
from tools import *


'''
Cette fonction vérifie si la base entrée est valide (2, 10 ou 16).
Elle retourne la base sous forme d'entier si elle est valide, sinon None.
'''
def check_base(base):
    if base in ["2", "10", "16"]:
        return int(base)
    else:
        print(ask_again_for_init_base_text)
        return None

'''
Cette fonction vérifie si le nombre entré est valide pour la base spécifiée.
Elle retourne True si le nombre est valide, False sinon.
'''
def is_valid_number(nombre, base):
    if base == 2:
        valid_chars = bin_valid_chars
    elif base == 10:
        valid_chars = dec_valid_chars
    elif base == 16:
        valid_chars = hex_valid_chars
    else:
        return False
    return all(char in valid_chars for char in nombre)

'''
Cette fonction vérifie si la base cible entrée est valide (2, 10 ou 16).
Elle retourne la base sous forme d'entier si elle est valide, sinon None.
'''
def check_target(target):
    if target in ["2", "10", "16"]:
        return int(target)
    else:
        print(ask_again_for_target_base_text)
        return None

'''
Cette fonction effectue la conversion du nombre entre les bases spécifiées.
Elle utilise les fonctions appropriées de conversion en fonction des bases d'entrée et de sortie.
'''
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

'''
Cette fonction gère le mode console du programme.
Elle demande à l'utilisateur les entrées nécessaires, effectue la conversion et affiche le résultat.
Elle permet également à l'utilisateur de continuer à faire des conversions ou de quitter le programme.
'''
def console_mode():
    while True:
        nombre = input(ask_for_init_number_text)
        base = input(ask_for_init_base_text)
        target = input(ask_for_target_base_text)

        init_base = check_base(base)
        target_base = check_target(target)
        
        if init_base is None or target_base is None:
            continue
        
        if not is_valid_number(nombre, init_base):
            print(ask_again_for_init_number_text)
            continue
        
        result = convert_base(nombre, init_base, target_base)
        print(f"{nombre} en base {init_base} est égale à {result} en base {target_base}")
        
        continuer = input("Voulez-vous convertir un autre nombre ? (oui/non): ").lower()
        if continuer != 'oui':
            break


if __name__ == "__main__":
    console_mode()