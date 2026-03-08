import math
import string

def calculate_entropy(password):
    charsetsize = 0
    if any(c.islower() for c in password):
        charsetsize+=26
    if any(c.isupper() for c in password):
        charsetsize+=26
    if any(c.isdigit() for c in password):
        charsetsize+=10
    if any(c in string.punctuation for c in password):
        charsetsize+=32
    
    entropy = len(password) *  math.log2(charsetsize)

    return round(entropy, 2)