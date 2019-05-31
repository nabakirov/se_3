class ConstantHolderMeta(type):
    @property
    def all(cls):
        resp = []
        for key in dir(cls):
            if key.isupper():
                resp.append(getattr(cls, key))
        return resp


class DBTable(metaclass=ConstantHolderMeta):
    UNIT = 'unit'
    MATERIAL = 'material'
    PRODUCT = 'product'
    POSITION = 'position'
    EMPLOYEE = 'employee'
    INGREDIENT = 'ingredient'
    BUDGET = 'budget'
    PURCHASE = 'purchase'
    SALE = 'sale'
    PRODUCTION = 'production'
    PAYROLL = 'payroll'
    CREDIT = 'credit'
    REPAYMENT = 'repayment'
