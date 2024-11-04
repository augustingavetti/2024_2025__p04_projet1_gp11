# bases:
bin_valid_chars = ["0", "1"]
dec_valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
hex_valid_chars = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","a","b","c","d","e","f"]

base_valid_chars = {'2': bin_valid_chars, '10': dec_valid_chars, '16': hex_valid_chars}

# questions et messages d'erreur
ask_for_init_base_text = "Entrez la base initial (2, 10, or 16): "
ask_again_for_init_base_text = "Base invalide. Svp entrez 2, 10, ou 16: "
ask_for_init_number_text = "Entrez le nombre initial: "
ask_again_for_init_number_text = "Nombre invalide pour la base donnée. Essayez à nouveau Svp: "
ask_for_target_base_text = "Entrez la base cible (2, 10, or 16): "
ask_again_for_target_base_text = "Base invalide. Entrez 2, 10 ou 16 :"