cipher = input("Enter ciphertext to brute-force: ")

for shift in range(26):
    result = []
    for ch in cipher:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)

    print(f"shift {shift:2}: {''.join(result)}")
