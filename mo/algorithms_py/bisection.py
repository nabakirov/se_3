
def f(X):
    return round(-0.04 * X ** 3 + X ** 2 + X -1, 4)



def bisection(a, b, tol, k_max, file=None):
    if file:
        print = file.write
    Fa, Fb = f(a), f(b)

    sign = lambda x: x > 0

    if sign(Fa) == sign(Fb):
        print("Sign on f(a) and f(b) must be opposite!\nCheck endpoints of the interval [a, b]!\n")
    else:
        k = 0
        print(f"{b-a}")
        while (b-a) > tol and k < k_max:
            k += 1
            m = a + (b - a) / 2
            Fa = f(a)
            Fm = f(m)

            if sign(Fa) == sign(Fm):
                a = m
            else:
                b = m
        print(
f'''Results:
    a = {a}
    b = {b}
    f(a) = {Fa}
    f(b) = {Fb}
    k = {k}''')


if __name__ == '__main__':
    a = 2
    b = -1
    k_max = 6
    tollerance = 0.2
    filename = './abakirov_bisection.txt'
    with open(filename, 'w+') as file:
        bisection(a, b, tollerance, k_max, file)



    

