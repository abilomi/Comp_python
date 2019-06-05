green_tea = 3
sushi_plates = 10

price_1 = 2.50
price_2 = 1.50

print("=======================================================")
print("green tea: $", str(green_tea * price_1))
print("sushi_plates: $", str(sushi_plates * price_2))

total = (green_tea * price_1) + (sushi_plates * price_2)
tip = 20/total

total_with_tip = total + tip

print("Total: $",total_with_tip)


