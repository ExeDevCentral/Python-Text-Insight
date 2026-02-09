text = input("Ingresa un texto a elección: ")
letters = []

text = text.lower()

letters.append(input("Ingresa la primera letra: ").lower())
letters.append(input("Ingresa la segunda letra: ").lower())
letters.append(input("Ingresa la tercera letra: ").lower())

print("\n" + "*" * 40)
print("RESULTADOS DEL ANÁLISIS")
print("*" * 40 + "\n")

# 1. Cantidad de letras
print("1. CANTIDAD DE LETRAS")
count1 = text.count(letters[0])
count2 = text.count(letters[1])
count3 = text.count(letters[2])

print(f"Hemos encontrado la letra '{letters[0]}' {count1} veces")
print(f"Hemos encontrado la letra '{letters[1]}' {count2} veces")
print(f"Hemos encontrado la letra '{letters[2]}' {count3} veces")

# 2. Cantidad de palabras
print("\n2. CANTIDAD DE PALABRAS")
words = text.split()
print(f"Hemos encontrado {len(words)} palabras en tu texto")

# 3. Primera y última letra
print("\n3. PRIMERA Y ÚLTIMA LETRA")
if text:
    print(f"La primera letra es '{text[0]}'")
    print(f"La última letra es '{text[-1]}'")
else:
    print("El texto está vacío.")

# 4. Texto invertido
print("\n4. TEXTO INVERTIDO")
words.reverse()
inverted_text = " ".join(words)
print(f"Si ordenáramos tu texto al revés diría: '{inverted_text}'")

# 5. Buscar la palabra Python
print("\n5. BUSCANDO LA PALABRA PYTHON")
is_python = 'python' in text
dic = {True: "sí", False: "no"}
print(f"La palabra 'Python' {dic[is_python]} se encuentra en el texto")
