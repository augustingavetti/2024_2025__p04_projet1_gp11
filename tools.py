def hex_math():
    pass
def bin_math():
    if init_base == "bin":
        def dec_to_bin(init_number):
            n = init_number
            result = ""
            while n > 0:
                result = str(n % 2) + result
                n = n // 2
            
            result += "+1" if init_number % 2 == 1 else "+0"
            
            return result