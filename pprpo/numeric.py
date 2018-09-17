import click


class BaseException(Exception):
    def __init__(self, message):
        self.message = message


@click.group()
def cli():
    pass



@click.command()
def another():
    print('another')




from py_expression_eval import Parser

class FormulaParser:
    exp = None
    raw = None
    parser = None

    def __init__(self, raw: str):
        self.raw = raw
        self.parser = Parser()

    def is_valid(self, raise_exception=False):
        exp = self.parser.parse(self.raw)
        vars = exp.variables()
        if len(vars) != 1:
            if raise_exception:
                raise Exception('must be only one variable "x"')
            return False
        if 'x' not in vars:
            if raise_exception:
                raise Exception('must be only one variable "x"')
            return False
        self.exp = exp
        return True


    def __call__(self, x):
        if not self.exp:
            raise Exception('cal .is_valid() first')
        return self.exp.evaluate({'x': x})




def secant_formula(x0, x, f):
    return (x0 * f(x) - x * f(x0)) / (f(x) - f(x0))




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


    fx0 = f(x0)
    fx1 = f(x1)
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
        fx = f(x)
        calc_e = abs(fx - _fx)
        _fx = fx


    print('n=', loop)
    print('x =', x)
    print('f(x0)=', _fx)
    print('e=', calc_e)
    return x



cli.add_command(secant)
cli.add_command(another)

if __name__ == '__main__':
    cli()