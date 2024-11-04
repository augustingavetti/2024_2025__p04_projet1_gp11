# bases:
bin_valid_chars = '01'
dec_valid_chars = '0123456789'
hex_valid_chars = '0123456789ABCDEFabcdef'

base_valid_chars = {'2': bin_valid_chars, '10': dec_valid_chars, '16': hex_valid_chars}

# questions et messages d'erreur
ask_for_init_base_text = "Entrez la base initial (2, 10, or 16): "
ask_again_for_init_base_text = "Base invalide. Svp entrez 2, 10, ou 16: "
ask_for_init_number_text = "Entrez le nombre initial: "
ask_again_for_init_number_text = "Nombre invalide pour la base donnée. Essayez à nouveau Svp: "
ask_for_target_base_text = "Entrez la base cible (2, 10, or 16): "
ask_again_for_target_base_text = "Base invalide. Entrez 2, 10 ou 16 :"
