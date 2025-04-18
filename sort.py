def sort(width, height, length, mass):
    #calculate volume
    volume = width * height * length


    #bulky condition
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    #return the result  
    return (
        "REJECTED" if is_bulky and is_heavy else
        "SPECIAL" if is_bulky or is_heavy else
        "STANDARD"
    )   

#test cases
print(sort(10, 10, 10, 10))           # STANDARD → Small dimensions and mass
print(sort(200, 100, 100, 10))        # SPECIAL → Width ≥ 150
print(sort(100, 100, 100, 25))        # SPECIAL → Heavy only
print(sort(200, 200, 200, 25))        # REJECTED → Both bulky and heavy
print(sort(150, 150, 150, 19.99))     # SPECIAL → Bulky only
print(sort(150, 150, 150, 200))       # REJECTED → Both


