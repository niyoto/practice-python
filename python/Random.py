import random
import string

#print(random.randint(1,100))
x = string.ascii_letters
y = string.digits
z = x + y
#print(z)

#a = random.sample(z,8)

#a = (random.choices(string.ascii_letters,k=5))
#b = (random.choices(string.digits,k=3))
#c = a + b
#print(a)
#print(b)
#print(c)

print("".join(random.sample(z,k=8)))