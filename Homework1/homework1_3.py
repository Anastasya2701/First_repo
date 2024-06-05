import re

def normalize_phone(phone_number):
    normalized_number = re.sub(r'[;/v+]', '', phone_number)

    if normalized_number.startswith('+'):
        return normalized_number
    elif normalized_number.startswith('380'):
        return '+' + normalized_number
    else:
        return '+380' + normalized_number
    
print(normalize_phone("965476809"))
    

