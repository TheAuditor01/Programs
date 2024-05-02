def bitwise_operations(string):
    and_string = ""
    or_string = ""
    xor_string = ""
    
    for char in string:
        char_int = ord(char)

        and_result = char_int & 127
        and_string += chr(and_result)
        
        or_result = char_int or 127
        or_string += chr(or_result)
        
        xor_result = char_int ^ 127
        xor_string += chr(xor_result)
    
    print("Original String:", string)
    print("\nBitwise AND with 127:", and_string)
    print("Bitwise OR with 127:", or_string)
    print("Bitwise XOR with 127:", xor_string)
    print('\n')

string = input('Enter String :- ')

bitwise_operations(string)
