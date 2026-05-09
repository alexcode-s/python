# Programa que pida por teclado 2 calificaciones numéricas de un alumno y muestre
# la media aritmética resultante redondeada sin decimales. Las notas introducidas
# deben estar entre 0 y 10 y admiten decimales. Caso de que una entrada sea
# errónea debería advertir sobre ello y no hacer el cálculo.

nums = []
nums.append(int(input("Numero 1: ")))
nums.append(int(input("Numero 2: ")))

valid = any(i >= 0  for i in nums) and any(i <= 10 for i in nums)

if valid:
    sum = nums[0] + nums[1]
    media = sum / 2

    print(round(media))
else:
    print("Numero invalido")