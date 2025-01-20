leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

grams_per_luoti = 13.3
grams_per_naula = 32 * grams_per_luoti
grams_per_leiviska = 20 * grams_per_naula

total_grams = (leiviska * grams_per_leiviska) + (naula * grams_per_naula) + (luoti * grams_per_luoti)
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"Massa nykymittojen mukaan:")
print(f"{kilograms} kilogrammaa ja {grams:.2f} grammaa.")