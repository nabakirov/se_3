from company.config import DBTable


class Role:
    DIRECTOR = DBTable.all
    MANAGER = (DBTable.SALE, DBTable.PURCHASE)
    TECHNOLOGIST = (DBTable.PRODUCTION, DBTable.PRODUCT, DBTable.MATERIAL, DBTable.UNIT, DBTable.INGREDIENT)
    ACCOUNTANT = (DBTable.EMPLOYEE, DBTable.PAYROLL, DBTable.CREDIT, DBTable.REPAYMENT)
    HR = (DBTable.EMPLOYEE, DBTable.POSITION)

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
        for title in cls.roles[role]:
            perms.append(f'company.add_{title}')
            perms.append(f'company.change_{title}')
            perms.append(f'company.delete_{title}')
            perms.append(f'company.view_{title}')
        return perms
