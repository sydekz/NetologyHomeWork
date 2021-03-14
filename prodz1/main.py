from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

if __name__ == '__main__':
    now_date_time = datetime.datetime.now()
    ddate = now_date_time.date()
    print(ddate)

    calculate_salary()
    get_employees()

