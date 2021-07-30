from stacks import Stack

def convert_int_to_bin(dec_num):

    remainders = Stack()
    quotient = dec_num // 2
    remainders.push(dec_num % 2)

    while quotient != 0:

        remainders.push(quotient % 2)
        quotient = quotient // 2
    
    intInBinary = ''

    while not remainders.is_empty():

        intInBinary += str(remainders.pop())
    
    return int(intInBinary)

print(convert_int_to_bin(2))
