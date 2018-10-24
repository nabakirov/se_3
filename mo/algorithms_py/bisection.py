
def f(X):
    return round(-0.04 * X ** 3 + X ** 2 + X -1, 4)



def bisection(a, b, tol, k_max, file=None):
    if file:
        print = file.write
    else:
        pass
    Fa, Fb = f(a), f(b)

    sign = lambda x: x > 0

    print(f"Iteration 0")
    print(f"a = {a}\n"\
          f"b = {b}\n"\
          f"tol = {tol}\n"\
          f"k_max = {k_max}\n"\
          f"Fa = f(a) = {Fa}\n"\
          f"Fb = f(b) = {Fb}\n"\
          f"sign(Fa) = sign(Fb) -> (Fa > 0) = (Fb > 0) -> ({Fa} > 0) = ({Fb} > 0)\t{sign(Fa) == sign(Fb)}\n\n")

    if sign(Fa) == sign(Fb):
        print("Sign on f(a) and f(b) must be opposite!\nCheck endpoints of the interval [a, b]!\n")
    else:
        k = 0
        while (b-a) > tol and k < k_max:
            k += 1
            m = round(a + (b - a) / 2, 4)
            Fa = f(a)
            Fm = f(m)
            print(f"Iteration {k}\n"\
                  f"1) k = {k}\n"\
                  f"2) m = a + (b - a) / 2 = {m}\n"\
                  f"   Fa = f(a) = {Fa}\n"\
                  f"   Fm = f(m) = {Fm}\n"\
                  f"3) sign(Fa) = sign(Fm) -> (Fa > 0) = (Fm > 0) -> ({Fa} > 0) = ({Fm} > 0)\t{sign(Fa) == sign(Fm)}\n")

            if sign(Fa) == sign(Fm):
                a = m
                print(f"\ta = m -> a = {m}\n")
            else:
                b = m
                print(f"\tb = m -> b = {m}\n")
            print(f"4) (b-a)>tol & k<k_max -> {round((b-a), 4)}>{tol} & {k}<{k_max}\t {round((b-a), 4) > tol and k < k_max}\n\n\n")
        print(
f'''Results:
    a = {a}
    b = {b}
    f(a) = {Fa}
    f(b) = {Fb}
    k = {k}''')


if __name__ == '__main__':
    a = -1.6
    b = 0.6
    k_max = 6
    tollerance = 0.01
    filename = './abakirov_bisection.txt'
    with open(filename, 'w+') as file:
        bisection(a, b, tollerance, k_max, file)



    

