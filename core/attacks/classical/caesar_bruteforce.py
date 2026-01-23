from core.primitives.classical.caesar import encrypt

cipher = input("Enter ciphertext to brute-force: ")

#Math-based brute force
for shift in range(26):
    result = []
    for ch in cipher:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)

    print(f"shift {shift:2}: {''.join(result)}")

#Encrypt misuse brute force 
for shift in range(26):
    print(shift, encrypt(cipher, -shift))
