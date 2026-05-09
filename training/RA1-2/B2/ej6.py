# Modificar ejercicio anterior para que la nota del boletín se redondee matemáticamente
# si es superior a 5 pero se trunquen los decimales si es inferior a 5.

nums = []
total = 0

for i in range(3): nums.append(float(input(f"Nota {i+1}: ")))

nums[0] = nums[0] * 0.05
nums[1] = nums[1] * 0.15
nums[2] = nums[2] * 0.8

for n in nums: total += n

print(f"Nota real: {total:.2f}")
print(f"Nota del boletín: {round(total)}" if total > 5 else f"Nota del boletín: {total:.0f}")