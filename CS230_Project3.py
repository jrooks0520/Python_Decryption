decrypt = ""
key = open('key.txt', 'r')
cipher = {}

for keyline in key:
    cipher[keyline.split()[1]] = keyline.split()[0]
key.close()
encrypted = open('encrypted.txt', 'r')
lines = encrypted.readlines()

for line in lines:
    for letter in line:
        letter = letter.upper()
        if letter.isalpha() == True:
            decrypt += cipher[letter]
        else:
            decrypt += letter

print(decrypt)

encrypted.close()
decryption = open("decrypted.txt", "w")
decryption.write(decrypt)
decryption.close()
