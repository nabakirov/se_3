from py_expression_eval import Parser


class FormulaParser:
    exp = None
    raw = None
    parser = None

    def __init__(self, raw: str, vars=['x']):
        self.raw = raw
        self.parser = Parser()
        self.variables = vars

    def is_valid(self, raise_exception=False):
        try:
            exp = self.parser.parse(self.raw)
        except Exception as e:
            if raise_exception:
                raise e
            return False
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


def main():
    f = FormulaParser('x^2+')
    valid = f.is_valid(raise_exception=False)
    if not valid:
        # Message box - invalid input
        print('invalid formula')
        return
    try:
        f(x=1)
    except Exception:
        # Message box - invalid input
        print('invalid formula')
        return
    print(f(x=3))


if __name__ == "__main__":
    main()