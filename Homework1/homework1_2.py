import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1:
        return[]
    elif max_num > 1000:
        return[]
    elif quantity < 1:
        return[]
    elif quantity > (max_num - min_num // 2):
        return[]
    else:
        ticket_numbers = random.sample(range(min_num,max_num // 2), quantity)
        ticket_numbers.sort()
        return ticket_numbers
    
lottery_numbers = get_numbers_ticket(29, 547, 8)
print("Ваші лотерейні числа:", lottery_numbers)
