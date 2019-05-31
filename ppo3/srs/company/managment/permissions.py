from managment.config import DBTable


class Role:
    DIRECTOR = DBTable.all
    MANAGER = (DBTable.SALE, DBTable.PURCHASE)
    TECHNOLOGIST = (DBTable.PRODUCTION, DBTable.PRODUCT, DBTable.MATERIAL, DBTable.UNIT, DBTable.INGREDIENT)
    ACCOUNTANT = (DBTable.EMPLOYEE, DBTable.PAYROLL, DBTable.CREDIT, DBTable.REPAYMENT)
    HR = (DBTable.EMPLOYEE,)

    roles = {
        'director': DIRECTOR,
        'manager': MANAGER,
        'technologist': TECHNOLOGIST,
        'accountant': ACCOUNTANT,
        'hr': HR
    }

    @classmethod
    def permission_list(cls, role):
        perms = []
        if role is None:
            return perms
        for title in cls.roles[role]:
            perms.append(f'managment.add_{title}')
            perms.append(f'managment.change_{title}')
            perms.append(f'managment.delete_{title}')
            perms.append(f'managment.view_{title}')
        return perms
