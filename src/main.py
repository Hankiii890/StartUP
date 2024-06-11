import sys
sys.path.append('/St_up/src')
from src.models import Defects, Employees
from src.models import session


def create_defects(code, defect, title, unit, headcount):
    tb_defect = Defects(code=code, defect=defect, title_work=title, unit_of_work=unit, headcount=headcount)
    session.add(tb_defect)
    session.commit()
    return tb_defect


def create_employees(empl_id, first_name, last_name, sheets_sent):
    tb_employees = Employees(employee_id=empl_id, first_name=first_name, last_name=last_name, sheets_sent=sheets_sent)
    session.add(tb_employees)
    session.commit()
    return tb_employees


def reade_defects():
    return session.query(Defects).all()


def reader_employees():
    return session.query(Employees).all()


def update_defects(id, code, defect, title, unit, headcount):
    defects = session.query(Defects).get(id)
    if defects:
        defects.code = code
        defects.defect = defect
        defects.title_work = title
        defects.unit_of_work = unit
        defects.headcount = headcount
        session.commit()
        return defect
    return None     # Не удалось найти дефект по казанному id


def update_employee(id, empl_id, first_name, last_name, sheets_sent):
    employees = session.query(Employees).get(id)
    if employees:
        employees.telegram_id = empl_id
        employees.first_name = first_name
        employees.last_name = last_name
        employees.sheets_sent = sheets_sent
        session.commit()
    return employees


def delete_defect(id):
    defect = session.query(Defects).get(id)
    if defect:
        session.delete(id)
        session.commit()


def delete_employee(id):
    employee = session.query(Employees).get(id)
    if employee:
        session.delete(id)
        session.commit()