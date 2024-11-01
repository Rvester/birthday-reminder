import random
import string

def generate_coupon():
    letters_and_digits = string.ascii_uppercase + string.digits
    coupon_code = ''.join(random.choices(letters_and_digits, k=10))
    return coupon_code