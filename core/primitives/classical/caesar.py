"""
The Caesar cipher is a simple substitution cipher that encrypts text by shifting
each letter a fixed number of positions along the alphabet.

This cipher is symmetric and uses a single integer shift as its key. Due to the
small key space and predictable letter frequencies, it is trivial to break using
brute-force or frequency analysis.

This implementation exists solely for educational purposes and should never be
used for real-world security.
"""

def encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypt plaintext using a Caesar cipher with a fixed shift.

    Parameters:
        plaintext (str): The input message consisting of alphabetic characters.
        shift (int): The number of positions to shift each letter.

    Returns:
        str: The resulting ciphertext after applying the shift.

    ToDo:
        Implement letter-wise shifting with wrap-around for the alphabet.
    """
    char_lst = [i for i in plaintext]
    reducer = shift % 26  # normalize shift to be within 0-25
    base_1 = ord('A')
    base_2 = ord('a')

    for i in range(len(char_lst)):
        if char_lst[i].isalpha():
            if char_lst[i].isupper():
                char_lst[i] = chr((ord(char_lst[i]) - base_1 + reducer) % 26 + base_1)
            else:
                char_lst[i] = chr((ord(char_lst[i]) - base_2 + reducer) % 26 + base_2)
    #In Python, modulo is defined so that the result has the same sign as the divisor.
    #a % b = a - b * floor(a / b)
    return ''.join(char_lst)

def decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypt ciphertext encrypted using a Caesar cipher with a fixed shift.

    Parameters:
    
        ciphertext (str): The encrypted message to be decrypted.
        shift (int): The shift value originally used during encryption.

    Returns:
        str: The recovered plaintext message.

    ToDo:
        Reverse the Caesar shift applied during encryption.
    """
    return encrypt(ciphertext, -shift)