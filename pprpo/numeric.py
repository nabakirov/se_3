import click
from py_expression_eval import Parser


class BaseException(Exception):
    def __init__(self, message):
        self.message = message


@click.group()
def cli():
    pass


class FormulaParser:
    exp = None
    raw = None
    parser = None

    def __init__(self, raw: str, vars=['x']):
        self.raw = raw
        self.parser = Parser()
        self.variables = vars

    def is_valid(self, raise_exception=False):
        exp = self.parser.parse(self.raw)
        vars = exp.variables()
        if len(vars) != len(self.variables):
            if raise_exception:
                raise Exception('must be only {}'.format(', '.join([v for v in self.variables])))
            return False
        for v in self.variables:
            if v not in vars:
                if raise_exception:
                    raise Exception('must be only one {}'.format(v))
                return False
        self.exp = exp
        return True

    def __call__(self, **kwargs):
        if not self.exp:
            raise Exception('cal .is_valid() first')
        return self.exp.evaluate(kwargs)

import sys
def input_digit():
    a = input()
    try:
        a = float(a)
    except:
        print('not a digit')
        sys.exit(0)
    else:
        return a


# def iteration():
#     f_count = input_digit()
#     funcs = {}
#     variables = {}
#     accuracy = {}
#     accuracy_passes = {}
#     for i in range(0, f_count):
#         funcs[i] = FormulaParser(input(), vars=['x'])
#         print("x0=".format(i))
#         variables[i] = input_digit()
#     print("e=")
#     e = input_digit()
#     i = 0
#     while 1:
        
        






@click.command()
def eiler():
    def eiler_formula(y, h, f):
        return y + h * f
    print("Formula f=")
    f = FormulaParser(input(), vars=['x', 'y', 'a', 'k'])
    try:
        f.is_valid(True)
    except Exception as e:
        print(e)
        return
    print('x0=')
    x0 = input_digit()
    print('y(0)=')
    y0 = input_digit()
    print('max x=')
    max_x = input_digit()
    print('a=')
    a = input_digit()
    print('k=')
    k = input_digit()
    print('h=')
    h = input_digit()

    x = x0
    y = y0
    i = 0
    while x <= max_x:
        i += 1
        x += h

        print('x{}='.format(i), x)
        calced = f(a=a, x=x, y=y, k=k)
        y = eiler_formula(y=y, h=h, f=calced)
        print('y{}='.format(i), y, '\n')








def newton_formula(prev_x, formula, derivative):
    return prev_x - (formula(x=prev_x) / derivative(x=prev_x))


@click.command()
def newton():
    print('Formula f=')
    raw_f = input()
    f = FormulaParser(raw_f)
    try:
        f.is_valid(True)
    except Exception as e:
        print(e)
        return
    print('derivative f`()=: ')
    derivative = FormulaParser(input())
    try:
        derivative.is_valid(True)
    except Exception as e:
        print(e)
        return
    print('x0: ')
    try:
        x0 = float(input())
    except ValueError:
        print('not a digit')
        return

    print('e: ')
    try:
        e = float(input())
    except ValueError:
        print('not a digit')
        return

    prev_x = x0
    calced_e = 99
    x = None
    loop = 0
    while 1:
        if calced_e < e:
            break
        x = newton_formula(prev_x, f, derivative)

        calced_e = abs(x - prev_x)
        prev_x = x

        loop += 1

    print('n=', loop)
    print('x =', x)
    print('e=', calced_e)
    return x





def secant_formula(x0, x, f):
    return (x0 * f(x=x) - x * f(x=x0)) / (f(x=x) - f(x=x0))




@click.command()
def secant():
    print('Formula x=')
    raw_f = input()
    f = FormulaParser(raw_f)
    try:
        f.is_valid(True)
    except Exception as e:
        print(e)
        return
    print('x0: ')
    try:
        x0 = float(input())
    except ValueError:
        print('not a digit')
        return
    print('x1: ')
    try:
        x1 = float(input())
    except ValueError:
        print('not a digit')
        return

    print('e: ')
    try:
        e = float(input())
    except ValueError:
        print('not a digit')
        return


    fx0 = f(x=x0)
    fx1 = f(x=x1)
    calc_e = abs(fx1 - fx0)
    # prev_f = fx1
    calc_e = 99
    x = x1
    _fx = fx1
    loop = 0
    while True:
        loop += 1
        # print(x, '\t', _fx, '\t', calc_e)
        if calc_e <= e:
            break
        x = secant_formula(x0, x, f)
        fx = f(x=x)
        calc_e = abs(fx - _fx)
        _fx = fx


    print('n=', loop)
    print('x =', x)
    print('f(x0)=', _fx)
    print('e=', calc_e)
    return x

def _k1_3(h, f, x, y, **kwargs):
    return h * f(**{**kwargs, "x":x, "y":y})

def _k2_3(h, f, x, y, k1, **kwargs):
    return h * f(**{**kwargs, "x": x + 1/2 * h, "y": y + 1/2 * k1})

def _k3_3(h, f, x, y, k1, k2, **kwargs):
    return h * f(**{**kwargs, "x": x + h, "y": y - k1 + 2 * k2})

def _kut_3(x, y, h, f, **kwargs):
    k1 = _k1_3(h, f, x, y, **kwargs)
    k2 = _k2_3(h, f, x, y, k1, **kwargs)
    k3 = _k3_3(h, f, x, y, k1, k2, **kwargs)
    return y + 1/6 * (k1 + 4 * k2 + k3), k1, k2, k3


def _k3_4(h, f, x, y, k2, **kwargs):
    return h * f(**{**kwargs, "x": x + 1/2 * h, "y": y + 1/2 * k2})

def _k4_4(h, f, x, y, k3, **kwargs):
    return h * f(**{**kwargs, "x": x + h, "y": y + k3})

def _kut_4(x, y, h, f, **kwargs):
    k1 = _k1_3(h, f, x, y, **kwargs)
    k2 = _k2_3(h, f, x, y, k1, **kwargs)
    k3 = _k3_4(h, f, x, y, k2, **kwargs)
    k4 = _k4_4(h, f, x, y, k3, **kwargs)
    return y + 1/6 * (k1 + 2 * k2 + k3 + k4), k1, k2, k3


def kut_(kut):
    print('Formula f=')
    raw_f = input()
    print('valiables')
    variables = [v.strip() for v in input().split()]
    f = FormulaParser(raw_f, vars=variables)
    try:
        f.is_valid(True)
    except Exception as e:
        print(e)
        return
    vars = {}
    for v in variables + ['max_x', 'h']:
        print("{}=".format(v))
        vars[v] = input_digit()
    

    x = vars.pop('x')
    y = vars.pop('y')
    max_x = vars.pop('max_x')
    h = vars.pop('h')

    i = 0
    while x <= max_x:
        i += 1
        x += h

        y, k1, k2, k3 = kut(x, y, h, f, **vars)

        print('''x{i}={x}\ny{i}={y}\n
                    \tk1={k1}\n
                    \tk2={k2}\n
                    \tk3={k3}\n'''.format(i=i, x=x, y=y, k1=k1, k2=k2, k3=k3))
    
    
@click.command()
def kut3():
    kut_(_kut_3)

@click.command()
def kut4():
    kut_(_kut_4)


cli.add_command(secant)
cli.add_command(newton)
cli.add_command(eiler)
cli.add_command(kut3)
cli.add_command(kut4)

if __name__ == '__main__':
    cli()