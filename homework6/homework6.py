apple = {"item": "Яблоко", "amount": 3, "price": "10"}
pear = {"item": "Груша", "amount": 0, "price": "14"}
plum = {"item": "Слива", "amount": 1, "price": "18"}

fruits = [apple, pear, plum]

def print_receipt(mass):
    final_price = 0
    total_amount = 0
    for item in mass:
        item_amount = item.get('amount')
        total_amount += item_amount
    if total_amount == 0:
        print("Вы ничего не купили...")
    else:
        for item in mass:
            if int(item.get('amount')) != 0:
                total_price = (int(item.get('amount')) * int(item.get('price')))
            
                print(f"{item.get('item')}   {item.get('amount')}  {item.get('price')}")
                print(f"                                    total: {total_price}")
                final_price += total_price
            else: pass
            
    print(f"Всего за чек: {final_price}")            
    
def print_total_price(mass):
    final_price = 0
    for item in mass:
        total_price = (int(item.get('amount')) * int(item.get('price')))
        final_price += total_price
    print(f"Всего за чек: {final_price}")  
    
def max_item_price(mass):
    price_list = {}
    
    for item in mass:
        if int(item.get('amount')) != 0:
            total_price = (int(item.get('amount')) * int(item.get('price')))
            price_list.update({item.get('item'): total_price})
    max_price = max(price_list.values())
    answear = max(price_list, key = price_list.get)        
    print(f"Сама дорогая ваша покупка - это {answear}, которая обошлась в {max_price}")

def average_cost(mass):
    final_price = 0
    total_amount = 0
    for item in mass:
        item_amount = item.get('amount')
        total_amount += item_amount
    for item in mass:
        total_price = (int(item.get('amount')) * int(item.get('price')))
        final_price += total_price
   
    average_price = final_price // total_amount
    print(f"Средняя стоимость товара в чеке составляет {average_price}")

def case_switch(n, mass = fruits):
    menu = {'1': print_receipt,\
            '2': print_total_price,\
            '3': max_item_price,\
            '4': average_cost}
    return(menu[n](mass))

print(" 1 - напечатать чек\n\
2 - посчитать общую стоимость чека\n\
3 - посчитать максимальную покупку в чеке\n\
4 - посчитать среднюю стоимость чека")

while True:
    n = input("\nВведите функцию, от 1 до 4:\n")
    print("\n")
    if n == '1':
        case_switch('1')
    elif n == '2':
        case_switch('2')
    elif n == '3':
        case_switch('3')
    elif n == '4':
        case_switch('4')
    else:
        break
    
