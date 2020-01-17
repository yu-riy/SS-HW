listing = ["false",1,0,1,2,0,1,3,"a"]

def moveZeros(lst):
    mass = []
    for i, each in enumerate(lst):
        if each == 0:
            mass.append(lst.pop(i))
    
    listing.extend(mass)
    print(listing)

    
moveZeros(listing)

# also works:
# mass = []
# [(lambda i: mass.append(listing.pop(i)))(i) for i, each in enumerate(listing) if each ==     listing.extend(mass)
# listing.extend(mass)
