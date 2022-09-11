

def exp(num, e):
    result = 1
    bin_rep = bin(e)[2:]
    for i, char in enumerate(bin_rep):
        if i == 0 and char == '1':
            result *= num
        elif char == '1':
            result = (result ** 2) * num
        elif char == '0':
            result **= 2
    return result


def exp_steps(e):
    if e == 0 or e == 1:
        return 0
    count = 0
    bin_rep = bin(e)
    for bit in bin_rep[3:]:
        if bit == '0':
            count += 1
        elif bit == '1':
            count += 2
    return count


def square_and_multiply_efficiency(e):
    return exp_steps(e) / (e - 1)

