# Listas de palabras en español e inglés
spanish_words = ["hola", "mundo", "de", "programadores"]
english_words = ["hello", "world", "of", "programmers"]

# Solicita al usuario ingresar una oración en español
input_text = input("Ingrese una oración en español: ")

# Divide la oración en palabras
palabras = input_text.split()

# Traduce cada palabra al inglés y las almacena en una lista
translated_words = []
for word in palabras:
    if word in spanish_words:
        translated_word = english_words[spanish_words.index(word)]
        translated_words.append(translated_word)
    else:
        translated_words.append(word)

# de inglés a español
english_to_spanish = input("Enter your english phrase: ")
words = english_to_spanish.split()
palabras_traducidas = []

for palabra in words:
    if palabra in english_words:
        palabra_traducida = spanish_words[english_words.index(palabra)]
        palabras_traducidas.append(palabra_traducida)
    else:
        palabras_traducidas.append(palabra)

# Construye la oración traducida
translated_sentence = ' '.join(translated_words)

# Imprime la oración original y la traducción
print("Oración ingresada:", input_text)
print("Traducción al inglés:", translated_sentence)
print("Traducción al español: ", ' '.join(palabras_traducidas))



