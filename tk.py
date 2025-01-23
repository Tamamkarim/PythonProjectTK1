import random


code1 = ""
for _ in range(3):
    digit = random.randint(0, 9)
    code1 += str(digit)
print(f"Arpoo kolmenumeroisen koodin: {code1}")


code2 = ""
for _ in range(4):
    digit = random.randint(1, 6)
    code2 += str(digit)
print(f"Arpoo nelinumeroisen koodin: {code2}")