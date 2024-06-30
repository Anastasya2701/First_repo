import re

def normalize_phone(number):
    number = re.sub(r'\D', '', number.strip())

    if not number.startswith('38'):
        number = '38' + number
    return '+' + number
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_nambers = [normalize_phone(num) for num in raw_numbers if num.strip]
print("Нормалізовані номери для SMS-розсилки:", sanitized_nambers)
    

