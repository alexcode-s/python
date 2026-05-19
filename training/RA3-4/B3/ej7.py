# Programa que pida por teclado una cadena de texto y la escriba con el alfabeto típico de hackers sustituyendo las
# letras "a" por el número 4, las letras "e" por el número 3, las letras "i" por el número 1 y las letras "o" por
# el número 0. Las vocales pueden estar en mayúsculas o minúsculas, pero no es necesario tener en cuenta que además
# pueden ir acentuadas.

cad = input("Cadena: ").strip()
nums = {'a': '4', 'e': '3', 'i': '1', 'o': '0'}
result = "".join(nums.get(c, c) for c in cad)
print(result)

