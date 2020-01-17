import re

#formula = "K4[ON(SO3)2]2"
#formula = "Mg(OH)2"
formula = "H2HOSiSiO2Mg4H3"

formula_depth = 1
for each in formula:
    if each in ["[","{","("]:
        formula_depth += 1

parsed_f = {}
for each, symbol in enumerate(formula):
    if symbol.isalpha() and symbol.isupper() and formula[(each+1)].isupper():
        if symbol not in parsed_f.keys():
            parsed_f[f"{symbol}"] = 1
        else:
            parsed_f[symbol] = int(parsed_f[symbol]) + 1
        
    if symbol.isalpha() and symbol.isupper() and formula[(each+1)].islower():
        x = symbol+formula[(each+1)]
        if x not in parsed_f.keys():
            parsed_f[x] = 1
        else:
           parsed_f[x] = int(parsed_f[x]) + 1
    if symbol.isalpha() and symbol.isupper() and formula[(each+1)].isdigit():
        if symbol not in parsed_f.keys():
            parsed_f[f"{symbol}"] = formula[(each+1)]
        else:
            parsed_f[symbol] =  parsed_f[symbol] + int(formula[(each+1)])

print(parsed_f)

    



