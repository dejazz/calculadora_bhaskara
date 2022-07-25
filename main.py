import math


a_info = input('Digite o valor de A ')
b_info = input('Digite o valor de B ')
c_info = input('Digite o valor de C ')


def delta(a, b, c):
    delta = pow(int(b),2) - 4 * int(a) * int(c)
    return int(delta)


def bhaskara(a, b, c):
    resultado_delta = int(delta(a, b, c))

    if resultado_delta < 0:
        return 'delta negativo'

    raiz_delta = round(math.sqrt(resultado_delta), 2)

    x1 = round((-int(b) + raiz_delta)/(2 * int(a)), 2)
    x2 = round((-int(b) - raiz_delta)/(2 * int(a)), 2)

    return f'x1={x1}, x2={x2}'


print(bhaskara(a_info, b_info, c_info))
