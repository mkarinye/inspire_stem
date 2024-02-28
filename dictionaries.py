laptop = {"make":"Dell", "colour": "black","weight":"1.1","year":"2023"}

print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

laptop["colour"] = "blue"
laptop["year"] = "2010"


"""
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)
"""

laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop["colour"]

print(laptop)

siz_laptop = laptop.copy
print(siz_laptop)

