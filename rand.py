
import random

cake = 1
pie = ""

while cake != 0:
    pie = ""
    while len(pie) != 40:
        pie = pie + str(random.randint(0,1))
    print(pie)
    
