from colored import bg

print("REDS = Refluxogenic Diet Score")
print("5 categories (1 - 5), the higher the category, the higher the refluxogenic potential of a food")
print("Please enter the nutritional values: ")
fat = float(input("Total Fat (g): "))
protein = float(input("Protein (g): "))
ph = float(input("pH: "))
if protein == 0:
    print("The value for protein must be greater than 0.")
    exit()
reds = round((fat / protein / 55 * 10 * (10 - ph)), 4)
if reds < 0.125:
    category = 1
    colour = 22
elif reds < 0.250:
    category = 2
    colour = 10
elif reds < 0.5:
    category = 3
    colour = 11
elif reds < 2:
    category = 4
    colour = 208
elif reds >= 2:
    category = 5
    colour = 1
else:
    category = None
    colour = 1
print("REDS = " + str(reds))
print("Category = " + str(category), end=" ")
print("{}  ".format(bg(colour)), end="")
