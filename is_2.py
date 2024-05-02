import math

def encrypt(msg, key):
    result = ""
    key_index = 0
    msg_length = float(len(msg))
    msg_list = list(msg)
    key_list = sorted(list(key))
    columns = len(key)
    rows = int(math.ceil(msg_length / columns))
    fill_null = int((rows * columns) - msg_length)
    msg_list.extend('_' * fill_null)
    matrix = [msg_list[i: i + columns] for i in range(0, len(msg_list), columns)]
    for _ in range(columns):
        current_index = key.index(key_list[key_index])
        result += ''.join([row[current_index] for row in matrix])
        key_index += 1
    return result

def decrypt(cipher, key):
    result = ""
    key_index = 0
    msg_index = 0
    msg_length = float(len(cipher))
    msg_list = list(cipher)
    columns = len(key)
    rows = int(math.ceil(msg_length / columns))
    key_list = sorted(list(key))
    decrypted_cipher = []
    for _ in range(rows):
        decrypted_cipher += [[None] * columns]
    for _ in range(columns):
        current_index = key.index(key_list[key_index])
        for j in range(rows):
            decrypted_cipher[j][current_index] = msg_list[msg_index]
            msg_index += 1
        key_index += 1
    try:
        result = ''.join(sum(decrypted_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    null_count = result.count('_')
    if null_count > 0:
        return result[: -null_count]
    return result

def main():
    key = input('\nEnter Key: ')
    choice = input("Enter 'e' for encryption or 'd' for decryption: ")
    if choice == 'e':
        msg = input('\nEnter Message to encrypt: ')
        encrypted_msg = encrypt(msg, key)
        print("\nEncrypted Message:", encrypted_msg,'\n')
    elif choice == 'd':
        cipher = input('\nEnter Cipher to decrypt: ')
        decrypted_msg = decrypt(cipher, key)
        print("\nDecrypted Message:", decrypted_msg,'\n')
    else:
        print("Invalid choice.")

main()
