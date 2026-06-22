# Atbash Şifrelemesi
def atbash_encrypt(plain_text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = plain_text.upper().replace(" ", "").replace(",", "").replace(".", "")
    encrypted_text = ""
    
    for char in plain_text:
        if char in alphabet:
            encrypted_text += alphabet[len(alphabet) - 1 - alphabet.index(char)]
        else:
            encrypted_text += char
    return encrypted_text

def atbash_decrypt(encrypted_text):
    return atbash_encrypt(encrypted_text)  # Atbash şifresi tersine çevrilerek çözülür.


# Vigenère Şifrelemesi
def vigenere_encrypt(plain_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = plain_text.upper().replace(" ", "").replace(",", "").replace(".", "")
    key = key.upper()
    encrypted_text = ""
    
    key_index = 0
    for char in plain_text:
        if char in alphabet:
            p = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            c = (p + k) % 26
            encrypted_text += alphabet[c]
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = encrypted_text.upper().replace(" ", "").replace(",", "").replace(".", "")
    key = key.upper()
    decrypted_text = ""
    
    key_index = 0
    for char in encrypted_text:
        if char in alphabet:
            c = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            p = (c - k) % 26
            decrypted_text += alphabet[p]
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text


# Playfair Şifrelemesi
def playfair_encrypt(plain_text, key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' harfi yok
    key = ''.join(sorted(set(key.upper()), key=lambda x: key.index(x)))  # Anahtar kelimenin benzersiz ve sıralanmış hali
    table = [key + alphabet for key in key]
    encrypted_text = ""
    plain_text = plain_text.upper().replace(" ", "").replace(",", "").replace(".", "").replace("J", "I")
    
    if len(plain_text) % 2 != 0:
        plain_text += "X"  # Eğer çift harf yoksa 'X' eklenir
    
    for i in range(0, len(plain_text), 2):
        a, b = plain_text[i], plain_text[i + 1]
        row_a, col_a = divmod(table.index(a), 5)
        row_b, col_b = divmod(table.index(b), 5)
        # Aynı satırda
        if row_a == row_b:
            encrypted_text += table[row_a][(col_a + 1) % 5] + table[row_b][(col_b + 1) % 5]
        # Aynı sütunda
        elif col_a == col_b:
            encrypted_text += table[(row_a + 1) % 5][col_a] + table[(row_b + 1) % 5][col_b]
        else:
            encrypted_text += table[row_a][col_b] + table[row_b][col_a]
    
    return encrypted_text


# Affine Şifrelemesi
def affine_encrypt(plain_text, a, b):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
    
    for char in plain_text.upper().replace(" ", "").replace(",", "").replace(".", ""):
        if char in alphabet:
            p = alphabet.index(char)
            c = (a * p + b) % 26
            encrypted_text += alphabet[c]
        else:
            encrypted_text += char
    
    return encrypted_text


# Skytale Şifrelemesi
def skytale_encrypt(plain_text, width):
    rows = [plain_text[i:i + width] for i in range(0, len(plain_text), width)]
    encrypted_text = ''.join([''.join(row[i] for row in rows if i < len(row)) for i in range(width)])
    return encrypted_text


# Transpozisyon Şifrelemesi
def transposition_encrypt(plain_text):
    plain_text = plain_text.replace(" ", "").replace(",", "").replace(".", "")
    n = len(plain_text)
    grid = [plain_text[i:i + 2] for i in range(0, n, 2)]
    encrypted_text = ''.join([grid[i][j] for i in range(len(grid)) for j in range(2)])
    return encrypted_text


# ROT13 Şifrelemesi
def rot13_encrypt(plain_text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
    
    for char in plain_text.upper().replace(" ", "").replace(",", "").replace(".", ""):
        if char in alphabet:
            index = (alphabet.index(char) + 13) % 26
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char
    
    return encrypted_text


# Polybius Şifrelemesi
def polybius_encrypt(plain_text):
    polybius_square = {"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16", "G": "17", "H": "18", "I": "19",
                       "K": "21", "L": "22", "M": "23", "N": "24", "O": "25", "P": "26", "Q": "31", "R": "32", "S": "33", "T": "34",
                       "U": "35", "V": "36", "W": "37", "X": "38", "Y": "39", "Z": "40"}
    encrypted_text = ""
    
    for char in plain_text.upper().replace(" ", "").replace(",", "").replace(".", ""):
        if char in polybius_square:
            encrypted_text += polybius_square[char]
    
    return encrypted_text


# Kullanıcıdan hangi işlemi yapmak istediği sorulur.
operation = input("Şifrelemek için 'E', şifreyi çözmek için 'C' tuşuna basın: ").upper()

# Şifreleme yöntemini seçmek için seçenekler sunulur.
method = input("Şifreleme yöntemi seçin (Atbash: A, Vigenere: V, Playfair: P, Affine: F, Skytale: S, Transpozisyon: T, ROT13: R, Polybius: Y): ").upper()

if method == 'A':
    if operation == 'E':
        plain_text = input("Lütfen şifrelemek istediğiniz metni girin: ")
        encrypted_text = atbash_encrypt(plain_text)
        print("Şifrelenmiş metin:", encrypted_text)
    elif operation == 'C':
        encrypted_text = input("Lütfen çözmek istediğiniz şifreli metni girin: ")
        decrypted_text = atbash_decrypt(encrypted_text)
        print("Çözülmüş metin:", decrypted_text)

elif method == 'V':
    if operation == 'E':
        plain_text = input("Lütfen şifrelemek istediğiniz metni girin: ")
        key = input("Lütfen anahtar kelimeyi girin: ")
        encrypted_text = vigenere_encrypt(plain_text, key)
        print("Şifrelenmiş metin:", encrypted_text)
    elif operation == 'C':
        encrypted_text = input("Lütfen çözmek istediğiniz şifreli metni girin: ")
        key = input("Lütfen anahtar kelimeyi girin: ")
        decrypted_text = vigenere_decrypt(encrypted_text, key)
        print("Çözülmüş metin:", decrypted_text)

elif method == 'P':
    if operation == 'E':
        plain_text = input("Lütfen şifrelemek istediğiniz metni girin: ")
        key = input("Lütfen anahtar kelimeyi girin: ")
        encrypted_text = playfair_encrypt(plain_text, key)
        print("Şifrelenmiş metin:", encrypted_text)
    elif operation == 'C':
        encrypted_text = input("Lütfen çözmek istediğiniz şifreli metni girin: ")
        key = input("Lütfen anahtar kelimeyi girin: ")
        # Çözme fonksiyonu henüz implement edilmediği için sadece şifreleme işlemi eklenmiştir
        print("Playfair çözme fonksiyonu eklenmedi.")

elif method == 'F':
    if operation == 'E':
        plain_text = input("Lütfen şifrelemek istediğiniz metni girin: ")
        a = int(input("Lütfen 'a' parametresini girin: "))
        b = int(input("Lütfen 'b' parametresini girin: "))
        encrypted_text = affine_encrypt(plain_text, a, b)
        print("Şifrelenmiş metin:", encrypted_text)
    elif operation == 'C':
        # Affine çözme fonksiyonu eklenmediği için sadece şifreleme işlemi eklenmiştir
        print("Affine çözme fonksiyonu eklenmedi.")
        
elif method == 'S':
    if operation == 'E':
        plain_text = input
