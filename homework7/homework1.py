import re

inp = "Pig latin, is cool."
z = re.findall("\w+|\W+", inp)
print(z)
#z[:] = [(lambds i: )()]
for i, each in enumerate(z):
    x = ''
    if str(each).isalpha() == True:
        print(each)
        x = str(each)[0]
        z[i] = z[i][1:]+ x + "ay"


print(" ".join(z))
