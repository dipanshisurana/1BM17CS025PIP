import string
import random
def passw(size, chars=string.ascii_letters + string.digits + string.punctuation):
 return ''.join(random.choice(chars)
                for _ in range(size))
print(passw(int(input('How many characters?\n'))))
