# TIC TAC TOE
import random

rand = 0

tic_tac = []
for row in range(0, 3):
    row = []
    tic_tac.append(row)
    
    for elem in range(0, 3):
        rand = random.randint(0,2)
        row.append(rand)


print(f"-------------")
print(f"|--{tic_tac[0][0]}--{tic_tac[0][1]}--{tic_tac[0][2]}--|")
print(f"-----------")
print(f"|--{tic_tac[1][0]}--{tic_tac[1][1]}--{tic_tac[1][2]}--|")
print(f"-----------")
print(f"|--{tic_tac[2][0]}--{tic_tac[2][1]}--{tic_tac[2][2]}--|")
print(f"-------------")

def count_tic_tac():      
    count_o = 0
    count_x = 0 
    count_zero = 0
    for raw in tic_tac:
        for elem in raw:
            if elem == 0:
                count_zero += 1
            if elem == 1:
                count_x += 1
            if elem == 2:
                count_o += 1

    
    if tic_tac[0][0] == tic_tac[0][1] == tic_tac[0][2] == 1 or\
       tic_tac[0][0] == tic_tac[1][0] == tic_tac[2][0] == 1 or\
       tic_tac[1][0] == tic_tac[1][1] == tic_tac[1][2] == 1 or\
       tic_tac[2][0] == tic_tac[2][1] == tic_tac[2][2] == 1 or\
       tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2] == 1 or\
       tic_tac[0][1] == tic_tac[1][1] == tic_tac[2][1] == 1 or\
       tic_tac[0][2] == tic_tac[1][2] == tic_tac[2][2] == 1 or\
       tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0] == 1:
            print("Победил Х")
            return
    elif tic_tac[0][0] == tic_tac[0][1] == tic_tac[0][2] ==2 or\
       tic_tac[0][0] == tic_tac[1][0] == tic_tac[2][0]  ==2 or\
       tic_tac[1][0] == tic_tac[1][1] == tic_tac[1][2]  ==2 or\
       tic_tac[2][0] == tic_tac[2][1] == tic_tac[2][2]  ==2 or\
       tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2]  ==2 or\
       tic_tac[0][1] == tic_tac[1][1] == tic_tac[2][1] == 2 or\
       tic_tac[0][2] == tic_tac[1][2] == tic_tac[2][2] == 2 or\
       tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0] == 2:
            print("Победил O")
            return
            
    if count_x == count_o:
        print("Игра продолжается, пока еще ничья!")
        return
    elif count_zero > 0:
        print("Победителя нет, игра продолжается!")
        
count_tic_tac()
