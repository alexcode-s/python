# Programa que pida al usuario su sueldo anual (decimales) y le informe del porcentaje de retención que le corresponde,
# el importe de la misma y el importe neto restante que cobrará.

salary = float(input("Sueldo: "))
bases = [12450, 20200, 35200, 60000, 300000]
ret = [0.19, 0.24, 0.3, 0.37, 0.45, 0.47]
ret_import = 0
net_import = 0

if salary > 0:
    pos = next((i for i, base in enumerate(bases) if salary <= base), -1)

    ret_import = ret[pos] * 100
    net_import = salary - (salary * ret[pos])

    print(f"Salario bruto: {salary} €")
    print(f"Porcentaje de retención: {ret_import}%")
    print(f"Importe retenido: {salary - net_import} €")
    print(f"Importe neto a cobrar: {net_import} €")
else:
    print("Salario introducido no válido")