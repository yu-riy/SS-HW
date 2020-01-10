def partition(number):
    
    answer = set()
    
    answer.add((number, ))
    
    for x in range(1, number):
       for y in partition(number - x):
           answer.add(tuple(sorted((x, ) + y)))
           
    return(answer)

n = input("Введите просто число больше 0 :\n")

result = list(partition(int(n)))

result_dict = {}       
for i, each in enumerate(result):
    #print(f"\n {result[i]}")
    mult = 1
    for number in each:
        
        mult *= number
    
    result_dict[i] = mult
    
end = max(result_dict, key = result_dict.get)
print(f"Максимальное произведение {result_dict.get(end)}, это элементы {result[end]}")
