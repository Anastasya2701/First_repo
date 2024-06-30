import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1:
        return[]
    elif max_num > 1000:
        return[]
    elif quantity < 1:
        return[]
    elif quantity > (max_num - min_num + 1):
        return[]
    else:
        ticket_numbers = random.sample(range(min_num,max_num + 1), quantity)
        ticket_numbers.sort()
        return ticket_numbers
    
lottery_numbers = get_numbers_ticket(10, 15, 5)
print("Ваші лотерейні числа:", lottery_numbers)
