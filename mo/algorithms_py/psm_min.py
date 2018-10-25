
import sys

sys.stdout = open('ular_psm_max.txt', 'w+')

def f(X):
    return round(-0.01 * X ** 3 + X ** 2 + X -1, 4)

x0 = 1
h0 = 4
r = 10
tol = 0.01
k_max = 6

def psm(x0=x0, h0=h0, r=r, tol=tol, k_max=k_max):
    yf0 = f(x0)
    h1 = h0
    x1 = x0 + h1
    yf1 = f(x1)
    k = 0
    print(f"Iteration 0.\n"\
          f"\tX0 = {x0}\n"\
          f"\tYF0 = f(X0) = {yf0}\n"\
          f"\tX1 = X0 + H1 = {x1}\n"\
          f"\tYF1 = f(X1) = {yf1}\n"\
          f"\tH0 = {h0}\n"\
          f"\tR = {r}\n"\
          f"\tTol = {tol}\n"\
          f"\tk_max = {k_max}\n")
    while k < k_max:
        k += 1
        print(f"Iteration {k}")
        print(f"1) k = {k}\n"\
              f"2) YF1 <= YF0 -> {yf1} <= {yf0}\t{yf1 <= yf0}")
        if yf1 <= yf0:
            print(f"3) abs(H0) < Tol / R -> {abs(h0)} < {tol/r}\t{abs(h0) < tol / r}")
            if abs(h0) < tol / r:
                h1 = h0
                x1 = x0
                yf1 = yf0
                print(f"4) H1 = H0 -> H1 = {h0}\n"\
                      f"   X1 = X0 -> X1 = {x0}\n"\
                      f"   YF1 = YF0 -> YF1 = {yf0}\n")
            else:
                h1 = -h0 / r
                h0 = h1

                x0 = x1
                yf0 = yf1
                x1 = x0 + h1

                yf1 = f(x1)
                print(f"4) H1 = -H0/R -> H1 = {h1}\n"\
                      f"   H0 = H1 -> H0 = {h0}\n"\
                      f"   x0 = x1 -> x0 = {x0}\n"\
                      f"   YF0 = YF1 -> YF0 = {yf0}\n"\
                      f"   x1 = x0 + H1 -> x1 = {x1}\n"\
                      f"   YF1 = f(x1) = {yf1}\n")
        else:
            h1 = h0
            x0 = x1
            yf0 = yf1
            x1 = x0 + h1

            yf1 = f(x1)
            print(f"3) H1 = H0 -> H1 = {h1}\n"\
                  f"   x0 = x1 -> x0 = {x0}\n"\
                  f"   YF0 = YF1 -> YF0 = {yf0}\n"\
                  f"   x1 = x0 + H1 -> x1 = {x1}\n"\
                  f"   YF1 = f(x1) = {yf1}\n")
        print(f"k < k_max -> {k} < {k_max}\t{k<k_max}\n\n\n")

    print(f"x1 = {x1}\n"\
          f"YF1 = {yf1}\n"\
          f"k = {k}\n"\
          f"H1 = {h1}\n")



if __name__ == '__main__':
    psm()
    