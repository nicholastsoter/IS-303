numbers = [14,2,3,45,5]

#Function
def isodd(numero):
    odd = True
    if numero % 2 == 0:
        odd = False
    return odd

#Main Program
for num in numbers:
    if isodd(num):
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

