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
        loop += 1
        if calced_e < e:
            break
        x = newton_formula(prev_x, f, derivative)

        calced_e = abs(x - prev_x)
        prev_x = x

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



cli.add_command(secant)
cli.add_command(newton)
cli.add_command(eiler)

if __name__ == '__main__':
    cli()